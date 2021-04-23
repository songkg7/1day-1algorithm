// 서울에서 김서방 찾기

var seoul = ["Jane", "ijf", "Kim"];
console.log(seoul.indexOf("Kim"));

function solution(seoul) {
  const x = seoul.indexOf("Kim");
  return `김서방은 ${x}에 있다`;
}

console.log(solution(seoul));
