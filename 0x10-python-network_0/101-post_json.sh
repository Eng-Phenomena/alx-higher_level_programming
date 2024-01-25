#!/bin/bash
# Sends a JSON POST request to a URL with a given JSON file.
curl -X POST -H "Content-Type: application/json" -d @"$json_file" "$url"
