#!/bin/bash
# a script that takes in a URL as an argument, sends a GET request to the URL
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
