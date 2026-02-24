#!/bin/bash
# Helper script to append to daily memory files
# Usage: ./scripts/memory-append.sh "content to append"
# Or: ./scripts/memory-append.sh -d YYYY-MM-DD "content to append"

MEMORY_DIR="memory"
DATE_ARG=""

# Parse arguments
if [[ "$1" == "-d" ]]; then
    DATE_ARG="$2"
    shift 2
else
    DATE_ARG="$(date +%Y-%m-%d)"
fi

CONTENT="$*"

if [[ -z "$CONTENT" ]]; then
    echo "Usage: $0 [-d YYYY-MM-DD] \"content to append\""
    echo "Example: $0 \"## New Entry\n- Something happened\""
    exit 1
fi

MEMORY_FILE="$MEMORY_DIR/$DATE_ARG.md"

# Create memory directory if it doesn't exist
mkdir -p "$MEMORY_DIR"

# Create file with header if it doesn't exist
if [[ ! -f "$MEMORY_FILE" ]]; then
    DATE_NAME=$(date -d "$DATE_ARG" +%A,\ %B\ %d,\ %Y 2>/dev/null || echo "$DATE_ARG")
    echo "# $DATE_NAME" > "$MEMORY_FILE"
    echo "" >> "$MEMORY_FILE"
fi

# Append content with a blank line separator
echo "" >> "$MEMORY_FILE"
echo "$CONTENT" >> "$MEMORY_FILE"

echo "✓ Appended to $MEMORY_FILE"
