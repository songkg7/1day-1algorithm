// 가운데 글자 가져오기

"a"; // 'a'
"ab"; // 'ab'
"abc"; // 'b'
"abcd"; // 'bc'
"abcde"; // 'c'
// 1 0
// 2 01
// 3 1
// 4 12
// 5 2
// 6 23
// 7 3
// 8 34

const s = "abcdffe";
function solution(s) {
  const div = s.length / 2;
  if (s.length % 2 === 1) {
    return s[parseInt(div)];
  } else {
    return s[div - 1] + s[div];
  }
}

// console.log(s.length);
console.log(solution(s));
