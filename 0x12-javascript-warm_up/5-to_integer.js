#!/usr/bin/node
const { argv } = require('node:process');

const a = Number(argv[2]);

if (isNaN(a)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + a);
}
