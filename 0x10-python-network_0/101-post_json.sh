#!/bin/bash
# a Bash script that sends a JSON POST request to a URL passed as the first argument
curl -s -X POST -H "Content-Type: application/json" "$1" -d @"$2"
