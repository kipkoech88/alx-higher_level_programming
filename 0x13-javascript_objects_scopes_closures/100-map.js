#!/usr/bin/node
const list = require('./100-data').list;

function printList (list) {
  const newList = list.map(function (x, y) {
    return x * y;
  }
  );
  return newList;
}

console.log(list);
console.log(printList(list));
