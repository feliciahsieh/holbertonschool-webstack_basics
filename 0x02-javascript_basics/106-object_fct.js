#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr () {
  myObject.value += 1;
}
myObject.incr = incr;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
