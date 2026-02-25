#!/bin/bash

# Serper.dev Web Search Script
# Usage: ./search.sh "query" [num_results]
# Example: ./search.sh "apple inc" 5

if [ -z "$1" ]; then
    echo "Usage: $0 \"search query\" [num_results]"
    exit 1
fi

# API key from environment or .env file
if [ -z "$SERPER_API_KEY" ]; then
    ENV_FILE="$(dirname "$0")/../../../.env"
    if [ -f "$ENV_FILE" ]; then
        SERPER_API_KEY=$(grep -oP '^SERPER_API_KEY=\K.*' "$ENV_FILE")
    fi
fi

if [ -z "$SERPER_API_KEY" ]; then
    echo "Error: SERPER_API_KEY not set. Set it in environment or in .env file."
    exit 1
fi

QUERY="$1"
NUM="${2:-5}"

RESPONSE=$(curl -s --location 'https://google.serper.dev/search' \
    --header "X-API-KEY: ${SERPER_API_KEY}" \
    --header 'Content-Type: application/json' \
    --data "{\"q\": \"${QUERY}\", \"num\": ${NUM}}")

if [ -z "$RESPONSE" ] || echo "$RESPONSE" | jq -e '.message' >/dev/null 2>&1; then
    echo "Error: $(echo "$RESPONSE" | jq -r '.message // "No response from API"')"
    exit 1
fi

# Display organic results
echo "$RESPONSE" | jq -r '
    (.organic // [])[] |
    "[\(.position // "?")] \(.title)\n    URL: \(.link)\n    \(.snippet // "No snippet")\n"
'

# Display knowledge graph if present
KG=$(echo "$RESPONSE" | jq -r '.knowledgeGraph.title // empty')
if [ -n "$KG" ]; then
    echo "--- Knowledge Graph ---"
    echo "$RESPONSE" | jq -r '.knowledgeGraph | "Title: \(.title)\nType: \(.type // "N/A")\nDescription: \(.description // "N/A")\n"'
fi
