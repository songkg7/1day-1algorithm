// 가장 큰 수

let numbers = [6, 10, 2];

function solution(numbers) {
  var answer = numbers
    .map((val) => String(val))
    .sort((a, b) => b + a - (a + b))
    .join("");
  return answer[0] === "0" ? "0" : answer;
}

console.log(solution(numbers));

// 숫자 배열을 문자열로 변환한다,
// 변환된 문자열을 비교정렬한다.
// join으로 하나의 단어로 묶는다.
