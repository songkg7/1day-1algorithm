// 문자열 내 마음대로 정렬하기

const strings = ["sun", "bed", "car"];
const n = 1;
// return ['car', 'bed', 'sun']

function solution(strings, n) {
  strings.sort((a, b) => {
    var first = a[n];
    var second = b[n];
    if (first === second) {
      return (a > b) - (a < b);
    } else {
      return (first > second) - (first < second);
    }
  });
  return strings;
}

console.log(solution(strings, n));

// 다른 풀이법

function solution1(strings, n) {
  return strings.sort((a, b) =>
    a[n] === b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n])
  );
}

console.log(solution1(strings, n));
