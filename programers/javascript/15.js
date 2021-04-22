// 이상한 문자 만들기
let s = "try hello world";
// console.log(s.split(" ")[0][2].toUpperCase());
// n%2 === 1 2n+1
function solution(s) {
  let result = s.split(" ");
  return result
    .map((n) =>
      n
        .split("")
        .map((w, i) => (i % 2 ? w.toLowerCase() : w.toUpperCase()))
        .join("")
    )
    .join(" ");
}

console.log(solution(s));

// Another Answer

function toWeirdCase(s) {
  return s.toUpperCase().replace(/(\w)(\w)/g, function (a) {
    return a[0].toUpperCase() + a[1].toLowerCase();
  });
}
