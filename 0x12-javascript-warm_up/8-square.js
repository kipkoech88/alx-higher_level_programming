#!/usr/bin/node
const { argv } = require('node:process');

const n = Number(argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    const fd = 'X';
    const rep = fd.repeat(n);
    console.log(rep);
  }
}
