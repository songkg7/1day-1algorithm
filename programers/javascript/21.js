// 제일 작은 수 제거하기

var arr = [10];
function solution(arr) {
  if (arr.length > 1) {
    return arr.filter((n) => n !== Math.min.apply(null, arr));
  }
  return [-1];
}

console.log(solution(arr));

// another answer

function solution1(arr) {
  arr.splice(arr.indexOf(Math.min(...arr)), 1);
  if (arr.length < 1) return [-1];
  return arr;
}
