#!/bin/bash
# submits data via post
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
