#!/usr/bin/node
dict = require('./101-data.js').dict
sorted = {};
temp = [];

for(var key in dict) {
  sorted[dict[key]] = key
  //let temp = dict.map(item => map.id);
  //console.log(temp)
  //sorted[dict[key]] = temp.push(key);
}

console.log(dict);
console.log(sorted);
