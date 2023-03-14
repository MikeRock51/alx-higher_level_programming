#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof (w) === 'number' && typeof (h) === 'number' && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    } else {
      return (this);
    }
  }
}

module.exports = Rectangle;
