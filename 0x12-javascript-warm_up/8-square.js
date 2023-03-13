#!/usr/bin/node

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(argv[2]); i++) {
    let width = '';
    for (let j = 0; j < Number(argv[2]); j++) {
      width += 'X';
    }
    console.log(width);
  }
}
