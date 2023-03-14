#!/usr/bin/node

/**
 * A rectangle Module
 */

class Rectangle {
  constructor (w, h) {
    if (typeof (w) === 'number' && typeof (h) === 'number' && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    } else {
      return (this);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
