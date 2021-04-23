// 자연수 뒤집어 배열로 만들기

let n = 12345;
console.log(String(n).split("").reverse());
function solution(n) {
  const x = String(n).split("").reverse();
  return x.map((v) => parseInt(v));
}
console.log(solution(n));
