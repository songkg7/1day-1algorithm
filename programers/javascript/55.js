// 큰 수 만들기

// 작은 숫자부터 차례대로 제거

let number = "1924";
let k = 2;

function solution(number, k) {
  var stack = []; // b : 최종 글자들이 저장될 스택 (숫자가 큰!)
  for (let i = 0; i < number.length; i++) {
    // 모든 숫자 비교
    var now = number[i]; // 현재 인덱스 숫자. 처음에는 그냥 push

    /* 무조건 push 하고 다음 for 문에서 이전 인덱스 숫자와 나랑 비교해서
    현재 인덱스가 이전 인덱스보다 크면 pop 하고 넣어줌.
    제거하는 숫자인 (k)를 1 감소
     */

    while (k > 0 && stack[stack.length - 1] < now) {
      stack.pop();
      k--;
    }
    stack.push(now);
  }
  // k가 0일 경우 스택은 그대로,
  // but k가 남아있으면 뒤에서부터 제거해준다. (ex. 1010,2 -> 11)(ex. 987,1 -> 98)
  stack.splice(stack.length - k, k);
  var answer = stack.join("");

  return answer;
}

console.log(solution(number, k));

// AA

function solution1(number, k) {
  const answer = [];
  let head = 0;
  let del = k;

  answer.push(number[head++]);
  while (answer.length < number.length - k || head < number.length) {
    if (del && answer[answer.length - 1] < number[head]) {
      answer.pop();
      del--;
      continue;
    }
    answer.push(number[head++]);
  }

  return answer.slice(0, number.length - k).join("");
}
