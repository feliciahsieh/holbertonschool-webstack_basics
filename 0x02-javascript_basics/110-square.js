#!/usr/bin/nodejs
const Square = require('./109-square').Square;

exports.Square = function Square (size) {
  Square.prototype.charPrint = function (c) {
    if (isNaN(c)) {
      c = 'X';
    }

    console.log('**c: ', c);
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  };
};
