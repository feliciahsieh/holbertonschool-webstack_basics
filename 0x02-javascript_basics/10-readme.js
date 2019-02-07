#!/usr/bin/node
var fs = require('fs');

try {
  fs.readFile(process.argv[2], 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
} catch (error) {
  console.log(error);
}
