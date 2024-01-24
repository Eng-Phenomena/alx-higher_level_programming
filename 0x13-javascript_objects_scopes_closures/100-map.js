#!/usr/bin/node
const li = require('./100-data').list;
console.log(li);
console.log(li.map((x, i) => x * i));
