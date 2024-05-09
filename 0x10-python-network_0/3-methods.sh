#!/bin/bash
# Display all available methods server accepts
curl -s -X OPTIONS "$1" | grep "Allow" | cut -f2- -d" "
