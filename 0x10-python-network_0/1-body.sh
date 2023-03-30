#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response if the status code is 200
curl -sf "$1"
