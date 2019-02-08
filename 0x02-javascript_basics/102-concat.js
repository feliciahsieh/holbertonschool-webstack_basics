#!/usr/bin/node
var fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err1, data1) {
  if (err1) {
    return console.log(err1);
  }
  fs.readFile(process.argv[3], 'utf8', function (err2, data2) {
    if (err2) {
      return console.log(err2);
    }
    fs.writeFile(process.argv[4], data1 + data2, 'utf8', function (err3) {
      if (err3) {
        return console.log(err3);
      }
    });
  });
});
