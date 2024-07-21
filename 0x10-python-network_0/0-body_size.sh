#!/bin/bash
# get the size of a response body size
curl -so /dev/null "$1" -w '%{size_download}\n'
