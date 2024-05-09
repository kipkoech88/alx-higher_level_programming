#!/bin/bash
# take in url and display size of response body
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
