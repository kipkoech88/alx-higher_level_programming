#!/bin/bash
# display the body with response code of 200

if [ "$(curl -L -s -X HEAD -w "%(http_code)" "$1")" == "200" ]; then curl -Ls "$1"; fi
