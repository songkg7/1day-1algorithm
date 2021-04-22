// 정수 제곱근 판별
const n = 143;

function solution(n) {
  if (n % Math.sqrt(n) === 0) {
    let x = Math.sqrt(n) + 1;
    return Math.pow(x, 2);
  } else return -1;
}

console.log(solution(n));
