// 숫자의 표현

// 홀수인 약수의 갯수와 같다

let n = 15;

function solution(n) {
  let answer = [];
  for (let i = 1; i <= n; i++) {
    if (n % i === 0 && i % 2 !== 0) {
      answer.push(i);
    }
  }
  return answer.length;
}

console.log(solution(n));

// AA

function expressions(num) {
  var answer = 0;
  var k = 0;

  while ((k * (k - 1)) / 2 <= num) {
    if (Number.isInteger(num / k - (k - 1) / 2) && num / k - (k - 1) / 2 != 0) {
      answer++;
    }
    k++;
  }

  return answer;
}
