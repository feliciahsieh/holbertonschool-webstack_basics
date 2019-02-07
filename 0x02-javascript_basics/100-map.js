#!/usr/bin/node
const list = require('./100-data').list;

var map = list.map((x, index) => x * index);

console.log(list);
console.log(map);
