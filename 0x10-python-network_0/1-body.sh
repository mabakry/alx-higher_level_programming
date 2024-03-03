#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the only 200 status code response
curl -sX GET $1 -L
