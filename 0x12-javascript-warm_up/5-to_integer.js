#!/usr/bin/node
const { argv } = process;

const convNum = parseInt(argv[2]);
if (isNaN(convNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convNum}`);
}
