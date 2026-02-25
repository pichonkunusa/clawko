#!/usr/bin/env python3
"""
Check AgentMail inbox for messages

Usage:
    # List recent messages
    python check_inbox.py --inbox "myagent@agentmail.to"
    
    # Get specific message
    python check_inbox.py --inbox "myagent@agentmail.to" --message "msg_123abc"
    
    # List threads
    python check_inbox.py --inbox "myagent@agentmail.to" --threads
    
    # Monitor for new messages (poll every N seconds)
    python check_inbox.py --inbox "myagent@agentmail.to" --monitor 30

Environment:
    AGENTMAIL_API_KEY: Your AgentMail API key
"""

import argparse
import os
import sys
import time
from datetime import datetime

try:
    from agentmail import AgentMail
except ImportError:
    print("Error: agentmail package not found. Install with: pip install agentmail")
    sys.exit(1)

def format_timestamp(iso_string):
    """Format ISO timestamp for display"""
    try:
        dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        return iso_string

def _getattr(obj, key, default=None):
    """Get attribute from object or dict"""
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)

def print_message_summary(message):
    """Print a summary of a message"""
    from_field = _getattr(message, 'from_') or _getattr(message, 'from') or []
    if from_field:
        first_from = from_field[0] if isinstance(from_field, list) else from_field
        if isinstance(first_from, str):
            from_addr = first_from
            from_name = ''
        else:
            from_addr = _getattr(first_from, 'email', '') or _getattr(first_from, 'address', str(first_from))
            from_name = _getattr(first_from, 'name', '')
    else:
        from_addr = 'Unknown'
        from_name = ''
    subject = _getattr(message, 'subject', '(no subject)')
    timestamp = format_timestamp(str(_getattr(message, 'created_at', '') or _getattr(message, 'timestamp', '')))
    preview = str(_getattr(message, 'preview', '') or _getattr(message, 'text', '') or '')[:100]

    print(f"📧 {_getattr(message, 'message_id', 'N/A')}")
    print(f"   From: {from_name} <{from_addr}>" if from_name else f"   From: {from_addr}")
    print(f"   Subject: {subject}")
    print(f"   Time: {timestamp}")
    if preview:
        print(f"   Preview: {preview}{'...' if len(preview) == 100 else ''}")
    print()

def print_thread_summary(thread):
    """Print a summary of a thread"""
    subject = _getattr(thread, 'subject', '(no subject)')
    participants = ', '.join(_getattr(thread, 'participants', []) or [])
    count = _getattr(thread, 'message_count', 0)
    timestamp = format_timestamp(str(_getattr(thread, 'last_message_at', '')))

    print(f"🧵 {_getattr(thread, 'thread_id', 'N/A')}")
    print(f"   Subject: {subject}")
    print(f"   Participants: {participants}")
    print(f"   Messages: {count}")
    print(f"   Last: {timestamp}")
    print()

def main():
    parser = argparse.ArgumentParser(description='Check AgentMail inbox')
    parser.add_argument('--inbox', required=True, help='Inbox email address')
    parser.add_argument('--message', help='Get specific message by ID')
    parser.add_argument('--threads', action='store_true', help='List threads instead of messages')
    parser.add_argument('--monitor', type=int, metavar='SECONDS', help='Monitor for new messages (poll interval)')
    parser.add_argument('--limit', type=int, default=10, help='Number of items to fetch (default: 10)')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = os.getenv('AGENTMAIL_API_KEY')
    if not api_key:
        print("Error: AGENTMAIL_API_KEY environment variable not set")
        sys.exit(1)
    
    # Initialize client
    client = AgentMail(api_key=api_key)
    
    if args.monitor:
        print(f"🔍 Monitoring {args.inbox} (checking every {args.monitor} seconds)")
        print("Press Ctrl+C to stop\n")

        last_message_ids = set()

        try:
            while True:
                try:
                    messages = client.inboxes.messages.list(
                        inbox_id=args.inbox,
                        limit=args.limit
                    )

                    new_messages = []
                    current_message_ids = set()

                    for message in messages.messages:
                        msg_id = _getattr(message, 'message_id')
                        current_message_ids.add(msg_id)

                        if msg_id not in last_message_ids:
                            new_messages.append(message)

                    if new_messages:
                        print(f"🆕 Found {len(new_messages)} new message(s):")
                        for message in new_messages:
                            print_message_summary(message)

                    last_message_ids = current_message_ids

                except Exception as e:
                    print(f"❌ Error checking inbox: {e}")

                time.sleep(args.monitor)

        except KeyboardInterrupt:
            print("\n👋 Monitoring stopped")
            return
    
    elif args.message:
        # Get specific message
        try:
            message = client.inboxes.messages.get(
                inbox_id=args.inbox,
                message_id=args.message
            )

            print(f"📧 Message Details:")
            print(f"   ID: {_getattr(message, 'message_id')}")
            print(f"   Thread: {_getattr(message, 'thread_id')}")

            from_field = _getattr(message, 'from_') or _getattr(message, 'from') or []
            if from_field:
                first_from = from_field[0] if isinstance(from_field, list) else from_field
                if isinstance(first_from, str):
                    from_addr, from_name = first_from, ''
                else:
                    from_addr = _getattr(first_from, 'email', '') or _getattr(first_from, 'address', str(first_from))
                    from_name = _getattr(first_from, 'name', '')
            else:
                from_addr, from_name = 'Unknown', ''
            print(f"   From: {from_name} <{from_addr}>" if from_name else f"   From: {from_addr}")

            to_field = _getattr(message, 'to', []) or []
            to_addrs = ', '.join([
                _getattr(addr, 'email', '') or _getattr(addr, 'address', str(addr))
                if not isinstance(addr, str) else addr
                for addr in to_field
            ])
            print(f"   To: {to_addrs}")

            print(f"   Subject: {_getattr(message, 'subject', '(no subject)')}")
            print(f"   Time: {format_timestamp(str(_getattr(message, 'created_at', '') or _getattr(message, 'timestamp', '')))}")

            labels = _getattr(message, 'labels', None)
            if labels:
                print(f"   Labels: {', '.join(labels)}")

            print("\n📝 Content:")
            text = _getattr(message, 'text', None)
            html = _getattr(message, 'html', None)
            if text:
                print(text)
            elif html:
                print("(HTML content - use API to get full HTML)")
            else:
                print("(No text content)")

            attachments = _getattr(message, 'attachments', None)
            if attachments:
                print(f"\n📎 Attachments ({len(attachments)}):")
                for att in attachments:
                    fname = _getattr(att, 'filename', 'unnamed')
                    ctype = _getattr(att, 'content_type', 'unknown type')
                    print(f"   • {fname} ({ctype})")

        except Exception as e:
            print(f"❌ Error getting message: {e}")
            sys.exit(1)
    
    elif args.threads:
        # List threads
        try:
            threads = client.inboxes.threads.list(
                inbox_id=args.inbox,
                limit=args.limit
            )

            thread_list = _getattr(threads, 'threads', []) or []
            if not thread_list:
                print(f"📭 No threads found in {args.inbox}")
                return

            print(f"🧵 Threads in {args.inbox} (showing {len(thread_list)}):\n")
            for thread in thread_list:
                print_thread_summary(thread)

        except Exception as e:
            print(f"❌ Error listing threads: {e}")
            sys.exit(1)

    else:
        # List recent messages
        try:
            messages = client.inboxes.messages.list(
                inbox_id=args.inbox,
                limit=args.limit
            )

            msg_list = _getattr(messages, 'messages', []) or []
            if not msg_list:
                print(f"📭 No messages found in {args.inbox}")
                return

            print(f"📧 Messages in {args.inbox} (showing {len(msg_list)}):\n")
            for message in msg_list:
                print_message_summary(message)

        except Exception as e:
            print(f"❌ Error listing messages: {e}")
            sys.exit(1)

if __name__ == '__main__':
    main()