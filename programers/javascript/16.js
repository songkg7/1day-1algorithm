// 자릿수 더하기

var n = 98234;
// console.log(n.split(""));

function solution(n) {
  return String(n)
    .split("")
    .reduce((prev, cur) => prev + +cur, 0); // +cur 로 숫자로 변환
  환;
}

console.log(solution(n));
