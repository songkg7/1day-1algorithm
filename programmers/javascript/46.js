// 키패드 누르기

let numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
let hand = "right";

function solution(numbers, hand) {
  // 거리 계산 함수
  let getDistanceXY = (xy1, xy2) =>
    Math.abs(xy1[0] - xy2[0]) + Math.abs(xy1[1] - xy2[1]);

  let curLeft = "*";
  let curRight = "#";

  // 숫자의 좌표
  let NumberXYObj = {
    1: [0, 0],
    2: [1, 0],
    3: [2, 0],
    4: [0, 1],
    5: [1, 1],
    6: [2, 1],
    7: [0, 2],
    8: [1, 2],
    9: [2, 2],
    "*": [0, 3],
    0: [1, 3],
    "#": [2, 3],
  };

  return numbers
    .map((number) => {
      if (number === 1 || number === 4 || number === 7) {
        curLeft = number;
        return "L";
      } else if (number === 3 || number === 6 || number === 9) {
        curRight = number;
        return "R";
      } else {
        // 2,5,8 일 경우 현재 손가락의 위치와 비교
        let distanceFromLeft = getDistanceXY(
          NumberXYObj[curLeft],
          NumberXYObj[number]
        );
        let distanceFromRight = getDistanceXY(
          NumberXYObj[curRight],
          NumberXYObj[number]
        );

        if (distanceFromLeft === distanceFromRight) {
          if (hand === "right") {
            curRight = number;
            return "R";
          }
          curLeft = number;
          return "L";
        } else if (distanceFromLeft < distanceFromRight) {
          curLeft = number;
          return "L";
        }
        curRight = number;
        return "R";
      }
    })
    .join("");
}

console.log(solution(numbers, hand));

// AA

const solution1 = (numbers, hand) => {
  const answer = [];

  let leftHandPosition = "*";
  let rightHandPosition = "#";

  numbers.forEach((number) => {
    if (number === 1 || number === 4 || number === 7) {
      answer.push("L");
      leftHandPosition = number;
      return;
    }

    if (number === 3 || number === 6 || number === 9) {
      answer.push("R");
      rightHandPosition = number;
      return;
    }

    const leftHandDistance = getDistance(leftHandPosition, number);
    const rightHandDistance = getDistance(rightHandPosition, number);

    if (leftHandDistance === rightHandDistance) {
      if (hand === "right") {
        answer.push("R");
        rightHandPosition = number;
        return;
      }

      if (hand === "left") {
        answer.push("L");
        leftHandPosition = number;
        return;
      }
    }

    if (leftHandDistance > rightHandDistance) {
      answer.push("R");
      rightHandPosition = number;
    }

    if (leftHandDistance < rightHandDistance) {
      answer.push("L");
      leftHandPosition = number;
    }
  });

  return answer.join("");
};

const getDistance = (locatedNumber, target) => {
  const keyPad = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    "*": [3, 0],
    0: [3, 1],
    "#": [3, 2],
  };

  const nowPosition = keyPad[locatedNumber];
  const targetPosition = keyPad[target];

  return (
    Math.abs(targetPosition[0] - nowPosition[0]) +
    Math.abs(targetPosition[1] - nowPosition[1])
  );
};
