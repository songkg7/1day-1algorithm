let price = [1, 2, 3, 2, 3];

// return = [4, 3, 1, 1, 0];

function solution(price) {
  let answer = [];

  for (let i = 0; i < price.length; i++) {
    answer.push(0); // 기본 값 설정
    for (let j = i + 1; j < price.length; j++) {
      if (price[j] >= price[i]) {
        answer[i] += 1;
      } else {
        answer[i] = 1;
        break;
      }
    }
  }

  return answer;
}

console.log(solution(price));
