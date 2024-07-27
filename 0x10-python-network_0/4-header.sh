#!/bin/bash
# script to send custom headers to servers
curl -s -H "X-Hello School!-User-Id: 98" "$1"
