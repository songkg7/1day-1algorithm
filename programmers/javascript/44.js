"use strict";
// printer

// shift(J)
// priority J<x ? push(j) : print(j)
let priorities = [2, 1, 3, 2];
let _location = 2;
// priorities[location] = my document
// priorities.shift(0) >
function solution(priorities, _location) {
  var answer = 1;
  var tIndex = _location;

  while (priorities.length > 0) {
    let J = priorities[0];
    priorities.shift(); // 가장 앞에 있는 문서를 추출

    // 중요도 높은 문서가 존재시 뒤로 넣음
    if (priorities.some((value) => value > J)) {
      priorities.push(J);
    } else {
      if (tIndex === 0) {
        break;
      } else answer++;
    }

    // 사용자가 선택한 문서가 중요도가 가장 높지 않은 경우 현재 대기열의 끝으로 index를 옮김
    if (tIndex === 0) tIndex = priorities.length - 1;
    else tIndex--;
  }
  return answer;
}

console.log(solution(priorities, _location));
