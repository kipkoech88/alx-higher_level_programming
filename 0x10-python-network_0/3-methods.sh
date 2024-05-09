#!/bin/bash
# Display all available methods server accepts
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -f 2- -d" "
