#!/bin/bash

# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL provided as an argument
URL="$1"

# Send a GET request to the URL with the custom header and display the response body
curl -s -H "X-School-User-Id: 98" "$URL"
