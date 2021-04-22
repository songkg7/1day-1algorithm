// 조이스틱

let name = "AABAAAAAAABBB";
// A가 첫문자와 마지막문자 사이에 있을경우 첫문자에서 커서를 왼쪽으로 움직여 마지막으로 이동이 가능하다
// 문자열에 A가 연속적으로 존재하는지를 체크한 후 코드를 실행해야한다

// console.log("A".charCodeAt());
// console.log("Z".charCodeAt());
// console.log(name.charCodeAt(0));
// console.log(String.fromCharCode(77));

function solution(name) {
  var answer = 0;
  var result = [];
  let count = 0;

  // 커서 이동시 드는값
  var reverseLength = 0;
  var length = 0;
  for (let i = 1; i < name.length; i++) {
    if (name[i] !== "A") {
      reverseLength = name.length - i;
      break;
    }
  }
  // console.log(reverseLength);

  for (let i = name.length - 1; i > 0; i--) {
    if (name[i] !== "A") {
      length = i;
      break;
    }
  }
  // console.log(length);
  if (length < reverseLength) {
    answer += length;
  } else {
    answer += reverseLength;
  }

  let code = name.split("").map((val) => val.charCodeAt());
  console.log(code);

  code.map((val) => {
    if (Math.abs(val - 65) < Math.abs(val - 91)) {
      result.push(Math.abs(val - 65));
    } else {
      result.push(Math.abs(val - 91));
    }
  });
  console.log(result);

  answer += result.reduce((prev, cur) => prev + cur, 0); // 알파벳 이동값들의 합

  //   for (let i = 0; i < code.length; i++) {}

  return answer;
}

console.log(solution(name));
console.log("-----------------------------");

// count 변수를 활용
// function solution1(name) {
//   var answer1 = 0;
//   let count = 0;
//   let code1 = name.split("").map((val) => val.charCodeAt());
//   console.log(code1);

//   return answer1;
// }

// console.log(solution1(name));

// AA
function solution1(name) {
  var answer = 0;
  var exp = name.length - 1; // 좌우로 움직여야하는 갯수
  var z = "Z".charCodeAt(0);
  var a = "A".charCodeAt(0);
  for (var i = 0; i < name.length; i++) {
    var c = name[i].charCodeAt(0);
    answer += z - c + 1 > c - a ? c - a : z - c + 1;
    if (c == a) {
      var nextIdx = i + 1;
      var countA = 0;
      while (nextIdx < name.length && name.charAt(nextIdx) == "A") {
        countA++;
        nextIdx++;
      }
      var tmp =
        (name.charAt(0) == "A" ? 0 : (i - 1) * 2) + // name의 첫 알파벳 또는 두번째 알파벳이 A이면 돌아갈 거리 및 오른쪽으로 움직일 필요가 없음으로 왼쪽으로 건너뜀.
        // *2 를 해주는 이유는 세번째 알파벳부터는 이전 알파벳(i-1)만큼 온거리를 돌아가는 거리.
        (name.length - (1 + i + countA)); // 현재 위치에서 A가 연속되는 갯수를 총길이에서 뺌. 처음 두번째 알파벳이 'A'일 경우 움직이는 최소거리.

      if (exp > tmp) exp = tmp;
    }
  }
  answer += exp;
  return answer;
}
