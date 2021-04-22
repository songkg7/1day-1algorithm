// 문자열 다루기 기본

const s = "1234";
console.log(s.length);

// var regex = /[^0-9]/g;

function solution(s) {
  return /^[0-9]+$/.test(s) && [4, 6].includes(s.length);
}

console.log(solution(s));

// 다른 풀이법

function alpha_string46(s) {
  var regex = /^\d{6}$|^\d{4}$/;
  return regex.test(s);
}
