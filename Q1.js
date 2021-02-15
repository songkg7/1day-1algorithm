// 두 개 뽑아서 더하기

let numbers = [2, 1, 3, 4, 1];

function solution(numbers) {
  let temp = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let addNumber = numbers[i] + numbers[j];
      temp.push(addNumber);
    }
  }

  const answer = [...new Set(temp)]; // spread
  return answer.sort((a, b) => a - b);
}

// function solution(numbers) {
//   let answer = [];

//   for (let i = 0; i < numbers.length; i++) {
//     for (let j = i + 1; j < numbers.length; j++) {
//       let addNumber = numbers[i] + numbers[j];
//       if (answer.indexOf(addNumber) === -1) {
//         answer.push(addNumber);
//       }
//     }
//   }
// //   console.log(answer.indexOf(10));
//   console.log(answer.sort((a, b) => a - b));
//   return answer.sort((a, b) => a - b);
// }

console.log(solution(numbers));
