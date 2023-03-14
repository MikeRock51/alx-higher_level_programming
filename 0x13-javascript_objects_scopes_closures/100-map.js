#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((currItem, idx) => {
  return (currItem * idx);
});

console.log(list);
console.log(newList);
