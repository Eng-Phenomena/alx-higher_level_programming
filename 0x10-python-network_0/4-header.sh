#!/bin/bash
# Bash Script that sends a GET request to a given URL with a header variable.
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
