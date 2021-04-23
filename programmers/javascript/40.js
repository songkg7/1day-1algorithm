// JadenCase 문자열 만들기

let s = "3people unFollowed me";

function solution(s) {
  return s
    .split(" ")
    .map((v) => {
      return v
        .split("")
        .map((val, index) => (index ? val.toLowerCase() : val.toUpperCase()))
        .join("");
    })
    .join(" ");
}

console.log(solution(s));

// AA

function solution1(s) {
  return s
    .split(" ")
    .map((v) => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase())
    .join(" ");
}
