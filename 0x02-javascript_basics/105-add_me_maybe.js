#!/usr/bin/nodejs
exports.addMeMaybe = function (number, theFunction) {
  return theFunction(number + 1);
};
