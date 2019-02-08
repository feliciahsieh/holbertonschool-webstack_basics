#!/usr/bin/node
const parentSquare = require('./109-square').Square;

exports.Square = function Square (size) {
  parentSquare.call(this, size);
};

exports.Square.prototype.charPrint = function (c) {
  if (typeof c === 'undefined') {
    c = 'X';
  }

  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};
