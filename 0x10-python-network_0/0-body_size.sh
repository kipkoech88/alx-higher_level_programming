#!/usr/bin/env bash
# take in url and display size of response body
curl -ls "$1" | grep -w 'Content-Length' | cut -f2 -d' '
