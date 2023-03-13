#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 2; i < argv.length; i++) {
    nums.push(argv[i]);
  }

  const sortedNum = nums.sort(function (a, b) {
    return (b - a);
  });

  console.log(sortedNum[1]);
}
