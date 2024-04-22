#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length > 2) {
  for (let i = 2; i < argv.length; i++) {
    console.log(argv[i]);
  }
} else {
  console.log('No argument');
}
