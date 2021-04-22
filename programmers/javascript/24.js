// 콜라츠 추측

var num = 16;

function solution(num) {
  let count = 0;
  for (let i = 1; i <= 500; i++) {
    if (i === 500) {
      return -1;
    }
    if (num === 1) {
      return count;
    } else if (num % 2 === 0) {
      num = num / 2;
      count++;
    } else {
      num = num * 3 + 1;
      count++;
    }
  }
  return count;
}

console.log(solution(num));

// switch, case 활용

// 재귀문 활용
function collatz(num, count = 0) {
  return num == 1
    ? count >= 500
      ? -1
      : count
    : collatz(num % 2 == 0 ? num / 2 : num * 3 + 1, ++count);
}
