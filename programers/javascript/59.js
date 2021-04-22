// 카펫 (완전탐색)

const brown = 10;
const yellow = 2;
// 가운데 노란격자가 있어야하므로 전체사각형 한 변의 길이는 항상 3보다 크거나 같다.
// 갈색과 노란색의 합은 사각형의 넓이(총 격자의 갯수)이다.
// 조건) 가로길이는 세로길이와 같거나, 길다

// 가로의 길이

// 세로의 길이

// 노란격자 가로의 길이 = 전체 가로길이 - 2
// 노란격자 세로의 길이 = 전체 세로길이 - 2

function solution(brown, yellow) {
  var answer = [];
  var sum = brown + yellow;

  for (let i = 1; i <= yellow; i++) {
    if (answer.some((e) => e[0] == i + 2)) continue; // 같은 값이 오면 무시
    if (Number.isInteger(yellow / i)) {
      // 인수분해 과정
      answer.push([yellow / i + 2, i + 2].sort((a, b) => b - a)); // 전체좌표의 값
    }
  }

  answer = answer.filter((e) => {
    if (e.reduce((a, b) => a * b) == sum) {
      return e;
    }
  });

  return answer.shift();
}

console.log(solution(brown, yellow));

// AA
function solution1(brown, yellow) {
  //   var answer = [];
  for (var i = 3; i <= (brown + yellow) / i; i++) {
    var x = Math.floor((brown + yellow) / i);
    if ((x - 2) * (i - 2) === yellow) {
      break;
    }
  }

  return [x, i];
}
