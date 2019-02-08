#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if ((w > 0) && (h > 0)) {
    this.width = w;
    this.height = h;
  }

  Rectangle.prototype.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  };
};
