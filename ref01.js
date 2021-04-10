// 1 부터 100 까지 순서대로 곱하기

let result = 1;
let i = 1;
function multiply(result) {
  if (i === 10) {
    return result;
  }

  i += 1;
  result *= i;
  return multiply(result);
}

console.log(multiply(result));
