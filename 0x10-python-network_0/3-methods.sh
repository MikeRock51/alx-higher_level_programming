#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sI "$!" | grep "Allow" | cut -d " " -f 2-
