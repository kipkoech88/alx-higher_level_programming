#!/usr/bin/node
const SquareP = require('./5-square.js');

class Square extends SquareP {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        const p = c;
        console.log(p.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
