#!/usr/bin/node
/*
 * reads contents of a file
 * and print output
 */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, cont) {
  console.log(err || cont);
});
