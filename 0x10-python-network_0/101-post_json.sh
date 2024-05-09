#!/bin/bash
# submits data via post
curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1"
