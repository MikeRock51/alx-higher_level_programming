#!/usr/bin/node

const argv = process.argv;

if (isNaN(parseInt(argv[2])) || argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log('C is fun');
  }
}
