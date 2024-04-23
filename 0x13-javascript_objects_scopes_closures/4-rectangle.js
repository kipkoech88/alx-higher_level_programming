#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const g = 'X';
      console.log(g.repeat(this.width));
    }
  }

  rotate () {
    const newHeight = this.width;
    const newWidth = this.height;
    this.width = newWidth;
    this.height = newHeight;
  }

  double () {
    const doubledW = this.width * 2;
    const doubledH = this.height * 2;
    this.width = doubledW;
    this.height = doubledH;
  }
}

module.exports = Rectangle;
