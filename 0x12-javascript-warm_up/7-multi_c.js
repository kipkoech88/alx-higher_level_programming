#!/usr/bin/node
const { argv } = require('node:process');

const n = Number(argv[2]);

if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
