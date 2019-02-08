#!/usr/bin/node
const Rectangle = require('./109-square').Square

class Square extends Square {
  Square.prototype.charPrint(c) = function () {
     if isNaN(c) {
      c = 'X';
    }
    for(let i=0;i<this.size;i++) {
      console.log(c.repeat(this.size));
    }
  }
}
