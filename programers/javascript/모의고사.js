function solution(answers) {
  let answer = [];
  let a = [1, 2, 3, 4, 5];
  let b = [2, 1, 2, 3, 2, 4, 2, 5];
  let c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let point = [0, 0, 0];
  for (let i = 0; i < answers.length; i++) {
    if (a[i % 5] == answers[i]) {
      point[0]++;
    }
    if (b[i % 8] == answers[i]) {
      point[1]++;
    }
    if (c[i % 10] == answers[i]) {
      point[2]++;
    }
  }
  let top = 0;
  for (let j = 0; j < point.length; j++) {
    if (point[j] > top) {
      top = point[j];
    }
  }
  for (let k = 0; k < point.length; k++) {
    if (top == point[k]) {
      answer.push(k + 1);
    }
  }
  return answer;
}

function solution(answers) {
  var answer = [];
  var a1 = [1, 2, 3, 4, 5];
  var a2 = [2, 1, 2, 3, 2, 4, 2, 5];
  var a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  var a1c = answers.filter((a, i) => a === a1[i % a1.length]).length;
  var a2c = answers.filter((a, i) => a === a2[i % a2.length]).length;
  var a3c = answers.filter((a, i) => a === a3[i % a3.length]).length;
  var max = Math.max(a1c, a2c, a3c);

  if (a1c === max) {
    answer.push(1);
  }
  if (a2c === max) {
    answer.push(2);
  }
  if (a3c === max) {
    answer.push(3);
  }

  return answer;
}
