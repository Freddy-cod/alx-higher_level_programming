#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL from the first argument
URL=$1

# Send GET request with header and display the response body
curl -s -H "X-School-User-Id: 98" "$URL"
