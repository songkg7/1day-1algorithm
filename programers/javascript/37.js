// 최솟값 만들기

let A = [1, 4, 2];
let B = [5, 4, 4];

function solution(A, B) {
  let answer = 0;
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  //   console.log(A[1] * B[1]);
  for (let i = 0; i < A.length; i++) {
    answer += A[i] * B[i];
  }
  return answer;
}
console.log(solution(A, B));

// AA
function solution1(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  return A.reduce((total, val, idx) => total + val * B[idx], 0);
}
