// 문자열을 정수로 바꾸기

const s = "1234";

console.log(Number(s));

function solution(s) {
  return parseInt(s.split("").join(""));
}
