// 문자열 내 p와 y 의 개수
var s = "yyppypp";
// [ '','' , 'pp', 'pp']
// console.log(s.split("y"));
// console.log(s.split("y").length);

// 정규표현식
function solution(s) {
  return s.match(/p/gi).length === s.match(/y/gi).length;
}

console.log(solution(s));
// 정확성 92%

// 다른 풀이법

function solution1(s) {
  return (
    s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length
  );
}

var solution = (s) =>
  (s.match(/p/gi) || []).length == (s.match(/y/gi) || []).length;

console.log(solution1(s));
