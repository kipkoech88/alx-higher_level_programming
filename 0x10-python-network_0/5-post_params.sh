#!/bin/bash
# post data to server via URL
curl -s -X POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
