// 정수 내림차순으로 배치하기
let n = 118372;

function solution(n) {
  return parseInt(
    n
      .toString()
      .split("")
      .sort((a, b) => b - a)
      .join("")
  );
}

console.log(solution(n));
