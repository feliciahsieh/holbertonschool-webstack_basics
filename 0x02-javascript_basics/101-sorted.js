#!/usr/bin/node
let dict = require('./101-data.js').dict;
let sorted = {};
let temp = [];

for (let key in dict) {
  if (sorted[dict[key]]) {
    sorted[dict[key]].push(key);
  } else {
    temp.push(key);
    sorted[dict[key]] = temp;
    temp = [];
  }
}

console.log(sorted);
