#!/usr/bin/node
const Rectangle = require('./107-rectangle').Rectangle;

exports.Square = function Square (size) {
  Rectangle.call(this, size, size);

  // inherit parent's prototype property
  Square.prototype = Object.create(Rectangle.prototype);

  Object.defineProperty(Square.prototype, 'constructor', {
    value: Square,
    enumerable: false, // so that it does not appear in 'for in' loop
    writable: true });
};
