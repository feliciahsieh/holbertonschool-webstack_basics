#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  this.width = w;
  this.height = h;

  Rectangle.prototype.width = function (w) {
    if (parseInt(w) === w) {
      this.width = w;
    }
  };

  Rectangle.prototype.height = function (h) {
    if (parseInt(h) === h) {
      this.height = h;
    }
  };
};
