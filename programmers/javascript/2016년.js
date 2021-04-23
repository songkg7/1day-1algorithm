console.log(new Date());

// const date = new Date(2016, 0, 1);
// month는 0~11 까지의 숫자가 입력되어야하고, 0 을 입력하면 1월임을 주의
// date.setFullYear(date.getFullYear() - 1);

// Question
const a = 5;
const b = 24;

function solution(a, b) {
  const answer = [];
  const week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];

  const date = new Date(2016, a - 1, b);
  answer.push(week[date.getDay()].toUpperCase());
  return answer[0];
}

// console.log(`기준일자 : ${date}`);
