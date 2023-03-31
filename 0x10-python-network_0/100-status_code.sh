#!/bin/bash
# Sends a curl request to the url passed as parameter and prints only the status code
curl -so /dev/null -w "%{http_code}" "$1"
