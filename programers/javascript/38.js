// 피보나치 수

let n = 3;

function solution(n) {
  const arr = [0, 1];
  for (let i = 1; i <= n; i++) {
    arr.push((arr[i - 1] + arr[i]) % 1234567);
  }
  return arr[n];
}

console.log(solution(n));

// AA
function fibonacci(num) {
  if (num < 2) return num;
  return fibonacci(num - 1) + fibonacci(num - 2);
}
