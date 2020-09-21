#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (let d = 0; d < list.length; d++) {
    if (list[d] === searchElement) {
      cnt++;
    }
  }
  return cnt;
};
