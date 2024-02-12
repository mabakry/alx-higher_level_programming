#!/usr/bin/node
const a = process.argv;
if (a.length <= 3) {
  console.log(0);
} else {
  console.log(a.sort((x, y) => y - x).slice(3)[0]);
}
