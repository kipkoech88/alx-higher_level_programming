#!/bin/bash
# Display only the status code
curl -sLw "%{http_code}" -o /dev/null "$1"
