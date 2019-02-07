#!/usr/bin/node
const add = require('./6-add').add;
console.log(add(3, 5));
console.log(add(3, -5));
console.log(add(3, '5'));
console.log(add(3, '-5'));
console.log(add(-3, 10));
console.log(add(-3, -5));
