#!/usr/bin/node
const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let d = 0; d < this.width; d++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
