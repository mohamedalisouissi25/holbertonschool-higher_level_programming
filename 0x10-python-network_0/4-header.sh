#!/bin/bash
# a script that takes in a URL as an argument, sends a GET request to the URL
curl -s -X -H "X-HolbertonSchool-User-Id: 98" "$1"
