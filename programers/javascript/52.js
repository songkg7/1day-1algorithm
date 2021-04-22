"use strict";

// 문자열 압축

let s = "aabbaccc";

function solution(s) {
  var answer = 0;
  let arrForNewStr = [];
  const len = s.length;

  // 1. 가능한 단위수 = 1~ 문자열의 개수/2 이하**
  // 각 단위수에서 압축된 문자열 구하기
  for (let i = 0; i < len; i++) {
    let num = i + 1; // 압축 기준 단위 수
    let count = 1; // 동일 글자가 몇 번 반복되는지
    let newStr = "";
    for (let j = 0; j < len; j += num) {
      let curSub = s.substring(j, j + num); // substring(a,b)
      let nextSub = s.substring(j + num, j + num + num);

      if (curSub === nextSub) {
        count++;
      } else {
        if (count !== 1) {
          newStr = newStr + count + curSub;
        } else {
          newStr = newStr + curSub;
        }
        count = 1; // count 초기화
      }
    }
    arrForNewStr.push(newStr.length);
  }
  answer = Math.min(...arrForNewStr);
  return answer;
}

console.log(solution(s));
