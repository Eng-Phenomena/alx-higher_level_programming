#!/usr/bin/node

const { argv } = require('process');
const args = argv.slice(2);
let result = 0, finalArray = [];

if (args.length > 1) {
  finalArray = [...new Set(args.map((x) => parseInt(x)).sort((a, b) => b - a))];
  result = finalArray.length > 1 ? finalArray[1] : finalArray[0];
}

console.log(result);
