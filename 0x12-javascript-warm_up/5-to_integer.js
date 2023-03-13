#!/usr/bin/node

const argv = process.argv;
const number = argv[2];

if (!isNaN(parseInt(number))) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
