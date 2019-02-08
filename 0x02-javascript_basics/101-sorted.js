#!/usr/bin/node
let dict = require('./101-data.js').dict;
let sorted = {};
// temp = [];

for (var key in dict) {
  sorted[dict[key]] = key;
  // let temp = dict.map(item => map.id);
  // console.log(temp)
  // sorted[dict[key]] = temp.push(key);
}

console.log(dict);
console.log(sorted);
