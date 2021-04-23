// 기능개발

let progresses = [93, 30, 55];
let speeds = [1, 30, 5];
// return = [2,1]

for (let i = speeds[0]; i < 100; i++) {}

function solution(progresses, speeds) {
  let answer = [];

  while (speeds.length > 0) {
    // 스피드 배열을 기준으로 0이되면 종료
    for (let i = 0; i < speeds.length; i++) {
      // 각 스피드에 맞게 기능을 하나씩 추가
      if (progresses[i] < 100) {
        progresses[i] += speeds[i];
      }
    }
    let deploy_count = 0;
    while (progresses[0] >= 100) {
      // 100이 넘으면 shift, 다음 기능이 100이 되어도 shift
      progresses.shift();
      speeds.shift();
      deploy_count++;
    }
    if (deploy_count > 0) {
      // 결과 배열에 넣어주기
      answer.push(deploy_count);
    }
  }
  return answer;
}

console.log(solution(progresses, speeds));

// AA
function solution1(progresses, speeds) {
  let answer = [0];
  let days = progresses.map((progress, index) =>
    Math.ceil((100 - progress) / speeds[index])
  );
  let maxDay = days[0];

  for (let i = 0, j = 0; i < days.length; i++) {
    if (days[i] <= maxDay) {
      answer[j] += 1;
    } else {
      maxDay = days[i];
      answer[++j] = 1;
    }
  }

  return answer;
}
