#!/bin/bash
# Display all available methods server accepts
curl -s -X OPTIONS "$1"
