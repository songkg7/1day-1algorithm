var num = 6;

function solution(num) {
  if (num % 2) {
    return "Odd";
  } else return "Even";
}

console.log(solution(num));

// another answer

function evenOrOdd(num) {
  return num % 2 ? "Odd" : "Even";
}
