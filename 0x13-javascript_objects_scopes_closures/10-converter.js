#!/usr/bin/Node
exports.converter = function (base) {
  return num => num.toString(base);
};
