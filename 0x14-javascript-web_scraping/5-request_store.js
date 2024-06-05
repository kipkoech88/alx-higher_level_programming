#!/usr/bin/node
// fs stream and pipe

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const pathTo = process.argv[3];

request(url).pipe(fs.createWriteStream(pathTo));
