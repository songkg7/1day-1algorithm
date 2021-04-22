// 하샤드 수

let x = 13;
function solution(x) {
  const Arrx = x.toString().split("");
  return !(x % Arrx.reduce((prev, cur) => parseInt(prev) + parseInt(cur), 0));
}

console.log(solution(x));
