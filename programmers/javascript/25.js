// 평균 구하기
let arr = [1, 2, 3, 4];
function solution(arr) {
  const n = arr.reduce((prev, cur) => prev + cur, 0);
  return n / arr.length;
}
// console.log(arr.length);
console.log(solution(arr));
