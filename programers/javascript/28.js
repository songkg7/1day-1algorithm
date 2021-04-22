// x만큼 간격이 있는 n개의 숫자

let x = -4;
let n = 2;
// result = [2,4,6,8,10]

function solution(x, n) {
  let answer = [x];
  for (let i = 0; i < n - 1; i++) {
    answer.push(answer[i] + x);
  }
  return answer;
}

console.log(solution(x, n));

// another answer

function solution1(x, n) {
  return Array(n)
    .fill(x)
    .map((v, i) => (i + 1) * v);
}
