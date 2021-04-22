// 최댓값과 최솟값

let s = "5 2 1 4";

function solution(s) {
  let test = s
    .split(" ")
    .map((val) => parseInt(val))
    .sort((a, b) => a - b);
  let result = [parseInt(test[0]), parseInt(test[test.length - 1])];
  return result.join(" ");
}
console.log(solution(s));

// AA
function solution1(s) {
  const arr = s.split(" ");

  return Math.min(...arr) + " " + Math.max(...arr);
}
