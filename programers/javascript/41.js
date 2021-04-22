// N개의 최소공배수

let arr = [2, 6, 8, 14];

function solution(arr) {
  return arr.reduce((prev, cur) => {
    function u(n, m) {
      return m % n ? u(m % n, n) : n;
    }
    return (prev * cur) / u(prev, cur);
  }, 1);
}

console.log(solution(arr));

// AA
var gcd = (a, b) => (b % a === 0 ? a : gcd(b % a, a));
var lcm = (a, b) => (a * b) / gcd(a, b);
var nlcm = (num) => num.sort().reduce((a, b) => lcm(a, b));
