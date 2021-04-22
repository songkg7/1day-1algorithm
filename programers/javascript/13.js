// 약수의 합

const n = 6;

function solution(n) {
  const arr = [];
  for (let i = 0; i <= n; i++) {
    if (n % i === 0) {
      arr.push(i);
    }
  }

  const answer = arr.reduce((prev, cur) => {
    return prev + cur;
  }, 0);
  return answer;
}

console.log(solution(n));

// 다른 풀이법

function solution2(n) {
  let arr1 = 0; // 변수의 재할당이 필요하므로 const 대신 let 을 사용한다
  for (let i = 0; i <= n; i++) {
    if (n % i === 0) {
      arr1 += i;
    }
  }
  return arr1;
}
console.log(solution2(n));
