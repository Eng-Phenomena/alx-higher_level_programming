#!/bin/bash
# Displays all HTTP methods that will be accepted by server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
