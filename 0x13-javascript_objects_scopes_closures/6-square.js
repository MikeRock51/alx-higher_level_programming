#!/usr/bin/node

/**
 * A square Module
 */

const firstSquare = require('./5-square');

class Square extends firstSquare {
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
