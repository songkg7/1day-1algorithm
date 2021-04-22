function solution(answers) {
  let answers = [];
  let a1 = [1, 2, 3, 4, 5];
  let;
}

function solution(answers) {
  let answer = []; //정답 출력
  let a1 = [1, 2, 3, 4, 5]; //반복주기 5
  let b1 = [2, 1, 2, 3, 2, 4, 2, 5]; // 반복주기 8
  let c1 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; //반복주기 10
  function max(a, b) {
    //최대값 함수
    if (a > b) return a;
    else return b;
  }
  let value = 0;
  let cnt = [0, 0, 0]; //수포자들의 점수
  for (var i = 0; i < answers.length; i++) {
    if (a1[i % 5] === answers[i]) cnt[0]++;
    if (b1[i % 8] === answers[i]) cnt[1]++;
    if (c1[i % 10] === answers[i]) cnt[2]++;
  }
  value = max(max(cnt[0], cnt[1]), cnt[2]); //최대값 입력
  var idx = 0;
  for (var i = 0; i < 3; i++) {
    //최대점수를 가진 수포자 찾기
    if (cnt[i] === value) {
      answer[idx] = i + 1;
      idx += 1;
    }
  }
  return answer;
}

// Another answer

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
