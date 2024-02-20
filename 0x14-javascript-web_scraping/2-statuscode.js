#!/usr/bin/node
const re = require('request');
re.get(process.argv[2]).on('response', function (response) { console.log(`code: ${response.statusCode}`); });
