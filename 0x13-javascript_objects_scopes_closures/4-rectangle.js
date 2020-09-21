#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let d = 0; d < this.height; d++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let rot = this.height;
    this.height = this.width;
    this.width = rot;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
