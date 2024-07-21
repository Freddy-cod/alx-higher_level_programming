#!/bin/bash
# displays all HTTP methods served in a endpoint
curl -sI $1 | grep Allow | cut -f 2- -d ' '
