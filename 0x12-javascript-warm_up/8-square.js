#!/usr/bin/node
const { argv } = process;

const convNum = parseInt(argv[2]);
if (isNaN(convNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convNum; i++) {
    console.log('x'.repeat(convNum));
  }
}
