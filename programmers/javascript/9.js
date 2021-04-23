// 소수 찾기

const n = 1000000;

function solution(n) {
  const answer = [];
  for (let i = 2; i <= n; i++) {
    let isPrimeNumber = true;
    for (let j = 2; j < i; j++) {
      if (i % j === 0) {
        isPrimeNumber = false;
        break;
      }
    }
    if (isPrimeNumber) {
      answer.push(i);
    }
  }
  return answer.length;
}

// console.log(solution(n));

// 효율성 개선을 위한 다른 풀이법
function isPrime(n) {
  if (n === 1) return false;

  if (n === 2) {
    return true;
  }

  /**
   * 2부터 주어진 자연수 n까지 모든 수를 하나씩 나누어도 같은 결과가 나오지만
   * 자연수 n의 약수 쌍의 경우, 반드시 둘 중 하나는 n 제곱근 이하이기 때문에
   * 제곱근까지만 나누어 확인할 경우 속도를 개선할 수 있다.
   */
  let size = Math.ceil(Math.sqrt(n));
  for (let i = 2; i <= size; i++) {
    if (n % i === 0) return false;
  }

  return true;
}

// 에라토스트테네스의 체를 활용
function solution2(n) {
  let answer = 0;
  let arr = [];

  let startTime = new Date();

  // 빈 배열에 값 초기화
  for (let i = 2; i <= n; i++) {
    arr[i] = i;
  }

  for (let i = 2; i <= n; i++) {
    if (arr[i] === 0)
      // 이미 체크된 수의 배수는 확인하지 않는다
      continue;

    for (let j = i + i; j <= n; j += i) {
      // i를 제외한 i의 배수들은 0으로 체크
      arr[j] = 0;
    }
  }

  // 0이 아닌 수들은 모두 소수이므로, answer을 증가한다.
  for (let i = 2; i <= n; i++) {
    if (arr[i] !== 0) answer++;
  }

  let endTime = new Date();
  let gapTime = endTime.getTime() - startTime.getTime();
  console.log("gapTime: ", gapTime + "ms");

  return answer;
}

console.log(solution2(n));
