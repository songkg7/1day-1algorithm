// 나누어 떨어지는 숫자 배열

var arr = [3, 2, 6];
var divisor = 10;

function solution(arr, divisor) {
  const a = arr.filter((n) => n % divisor === 0).sort((a, b) => a - b);
  if (a[0] != undefined) {
    return a;
  } else {
    a.push(-1);
    return a;
  }
}
console.log(solution(arr, divisor));

// 다른 풀이법

function solution1(arr, divisor) {
  var answer = arr.filter((v) => v % divisor == 0);
  return answer.length == 0 ? [-1] : answer.sort((a, b) => a - b);
}
