#!/usr/bin/node

const argv = process.argv;

function factos (n) {
  if (n < 0) {
    return (NaN);
  } else if (n === 1 || isNaN(n)) {
    return (1);
  } else {
    return (n * factos(n - 1));
  }
}

console.log(Number(factos(argv[2])));
