#!/usr/bin/node
exports.add = function add (a, b) {
  try {
    if ((parseInt(a) === a) && (parseInt(b) === b)) {
      return a + b;
    } else {
      console.log('Error: Not a number');
      return NaN;
    }
  } catch (error) {
    console.log(error);
  }
};
