#!/usr/bin/node

exports.esrever = function (list) {
  const array = [];
  for (let d = 0; d < list.length; d++) {
    array.unshift(list[d]);
  }
  return array;
};
