// 최대공약수와 최소공배수

var n = 3;
var m = 12;
//  result = [3, 12];

// 유클리드 호제법, 두 수의 곱은 초대공약수와 최소공배수의 곱과 같다
function solution(n, m) {
  function u(n, m) {
    return m % n ? u(m % n, n) : n;
  }
  const gcd = u(n, m);
  return [gcd, (n * m) / gcd];
}
console.log(solution(n, m));
