// 올바른 괄호

let s = "()";

function solution(s) {
  let count = 0;
  if (s[0] === ")" || s[s.length - 1] === "(") {
    return false;
  }
  for (let i = 0; i < s.length; i++) {
    s[i] === "(" ? count++ : count--;
    if (count < 0) return false; // '(' 보다 ')' 가 더 많아지는 순간 false 를 리턴
  }
  return count === 0 ? true : false;
}

console.log(solution(s));
