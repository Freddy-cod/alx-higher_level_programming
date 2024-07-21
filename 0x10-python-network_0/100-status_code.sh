#!/bin/bash
# sends a request to a URL passed as an argument, and displays the status .
curl -w '%{response_code}' "$1" -so /dev/null
