#!/usr/bin/node
if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(1);
} else {
  let max = parseInt(process.argv[2]);
  let secondMax = Number.MIN_SAFE_INTEGER;

  for (let i = 3; i <= process.argv.length; i++) {
    if (max <= parseInt(process.argv[i])) {
      secondMax = max;
      max = parseInt(process.argv[i]);
    } else if (secondMax < parseInt(process.argv[i])) {
      secondMax = parseInt(process.argv[i]);
    }
  }
  console.log(secondMax);
}
