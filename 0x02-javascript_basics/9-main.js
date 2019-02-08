#!/usr/bin/node
const Rectangle = require('./9-rectangle').Rectangle;

console.log('default:');
const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

console.log('main_0:');
const r3 = new Rectangle(3, 3);
console.log(r3);
console.log(r3.width);
console.log(r3.height);
r3.print();

console.log('main_1:');
const r4 = new Rectangle(3, 10);
console.log(r4);
console.log(r4.width);
console.log(r4.height);
r4.print();

console.log('main_2:');
const r5 = new Rectangle(10, 3);
console.log(r5);
console.log(r5.width);
console.log(r5.height);
r5.print();
