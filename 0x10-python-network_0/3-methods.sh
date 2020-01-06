#!/bin/bash
# script that takes a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep "allow" | cut -d " " -f 2-
