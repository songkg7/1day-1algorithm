// 같은 숫자는 싫어

const arr = [1, 1, 3, 3, 0, 1, 1];
function solution(arr) {
  const answer = []; // 처음 숫자는 무조건 배열에 속함.
  for (let i in arr) {
    if (arr[i - 1] !== arr[i]) {
      answer.push(arr[i]);
      // 앞에 있는 숫자와 비교 후 다르면 push
    }
  }
  return answer;
}

console.log(solution(arr));

// 다른 사람들의 풀이법
// function solution(arr) {
//   return arr.filter((val, index) => val != arr[index + 1]);
// }

function solution1(arr) {
  return arr.filter((val, index) => val !== arr[index + 1]);
}
console.log(solution1(arr));
