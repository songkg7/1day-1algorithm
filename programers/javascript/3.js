const a = 1;
const b = 10;
// return = 12

function solution(a, b) {
  var answer = 0;
  var small, big;
  if (a > b) {
    big = a;
    small = b;
  } else if (b > a) {
    big = b;
    small = a;
  } else {
    answer = a;
  }

  for (let i = small; i <= big; i++) {
    answer += i;
  }
  return answer;
}

// console.log(arr);
console.log(solution(a, b));

// 다른 풀이법

function adder(a, b) {
  var result = 0;
  return ((a + b) * (Math.abs(b - a) + 1)) / 2;
}

console.log(adder(a, b));
