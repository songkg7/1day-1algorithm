// 문자열 내림차순으로 배열하기
const s = "Zbcdefg";
function solution(s) {
  return (
    s
      .split("")
      .sort((prev, cur) => cur.charCodeAt() - prev.charCodeAt())
      // 문자열을 유니코드로 치환한 후 내림차순으로 정렬한다
      .join("")
  ); // 구분자를 주지 않고 결과값을 받는다
}

console.log(solution(s));

// 다른 풀이법

function solution1(s) {
  return s.split("").sort().reverse().join("");
}

console.log(solution1(s));
