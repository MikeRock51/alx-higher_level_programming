#!/bin/bash
# Sends a POST request using curl to a given url, parsing json data from a given file
curl -sH "content-type: application/json" -d @"$2" "$1"
