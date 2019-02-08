#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

Object.prototype.incr = function () {
  this.value += 1;
}
myObject.incr = incr;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
