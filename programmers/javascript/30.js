// 124 나라의 숫자
"use strict";

let n = 6;

function solution(n) {
  var answer = "";
  var residue = 0;
  var period = ["4", "1", "2"];

  while (n > 0) {
    residue = n % 3;
    n = parseInt(n / 3);

    if (residue === 0) {
      n = n - 1;
    }
    answer = period[residue] + answer;
  }
  return answer;
}

console.log(solution(n));
console.log(parseInt(n / 3));

// another answer
function change124(n) {
  return n === 0
    ? ""
    : change124(parseInt((n - 1) / 3)) + [1, 2, 4][(n - 1) % 3];
}
