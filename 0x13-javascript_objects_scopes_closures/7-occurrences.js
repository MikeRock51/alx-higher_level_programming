#!/usr/bin/node

/**
 * A square Module
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) { c = 'X'; }

    for (let i = 0; i < this.width; i++) {
      // console.log("WIII");
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
