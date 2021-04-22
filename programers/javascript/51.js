// 다트 게임

const dartResult = "1S2D*3T";
// answer = 37;

function solution(dartResult) {
  var dr = dartResult.match(/\d{1,2}[SDT]{1}[*|#]?/g);
  //   console.log(dr);
  var score = [];
  for (var i = 0; i < 3; i++) {
    var num = dr[i].match(/\d{1,2}/g);
    var ch = dr[i].match(/[SDT]{1}/g);
    var kiho = dr[i].match(/[*|#]/g);

    switch (
      ch[0] // SDT 가 연속된 경우는 없기 때문에 배열은 항상 하나의 값만 존재한다
    ) {
      case "S":
        num = parseInt(num);
        break;
      case "D":
        num = Math.pow(num, 2);
        break;
      case "T":
        num = Math.pow(num, 3);
        break;
    }

    if (kiho == "*") {
      // 배열안에 기호가 있고 null인 경우가 있기 때문에 === 이 아닌 == 연산자로 비교한다
      num = num * 2; // 해당 점수 2배
      if (i !== 0) {
        score[i - 1] = score[i - 1] * 2; // 첫번째 숫자가 아닐시 바로 전의 점수도 2배
      }
    } else if (kiho == "#") {
      num = num * -1; // #이 나올시 해당점수 -
    }
    score.push(num);
  }
  //   console.log(score);
  return score.reduce((prev, cur) => prev + cur, 0);
}

console.log(solution(dartResult));
// console.log(Math.pow(2, 3));

// AA
