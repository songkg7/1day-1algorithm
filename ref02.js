let strings = ["abce", "abcd", "cdx"];

let n = 2;

// ["car", "bed", "sun"]

function solution(strings, n) {
  return sort((a, b) =>
    a[n] === b[n] ? b.localeCompare(a) : a[n].localeCompare(b[n])
  );
}

console.log(solution(strings, n));
