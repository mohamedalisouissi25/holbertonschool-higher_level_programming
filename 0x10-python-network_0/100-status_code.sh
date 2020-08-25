#!/bin/bash
# Send request to a URL and displays only the status code
curl -sLI -o /dev/null -w '%{http_code}' "$1"
