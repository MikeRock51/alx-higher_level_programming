#!/usr/bin/node

const argv = process.argv;
const number = argv[2];

if (number !== undefined && typeof (Number(number)) === 'number') {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
