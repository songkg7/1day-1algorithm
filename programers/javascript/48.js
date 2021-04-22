// 예산
let d = [2, 2, 3, 3];
let budget = 10;

function solution(d, budget) {
  var answer = 0;
  d.sort((a, b) => a - b).reduce((prev, cur) => {
    if (prev + cur <= budget) {
      answer++;
      return prev + cur;
    }
  }, 0);
  return answer;
}

console.log(solution(d, budget));
