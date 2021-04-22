// 비밀지도

const n = 5;
const arr1 = [9, 20, 28, 18, 11];
const arr2 = [30, 1, 21, 17, 28];
// result = ['#####','# # #', '### #', '# ##','#####']

// console.log(result);

function solution(n, arr1, arr2) {
  var answer = [];
  for (let i = 0; i < n; i++) {
    const bin = (arr1[i] | arr2[i]).toString(2);
    const line = [];
    for (let j = bin.length - n; j < bin.length; j++) {
      if (bin[j] === "1") {
        line.push("#");
      } else {
        line.push(" ");
      }
    }
    answer.push(line.join(""));
  }
  return answer;
}

console.log(solution(n, arr1, arr2));

// AA

function solution1(n, arr1, arr2) {
  return arr1.map((v, i) => {
    const line = (v | arr2[i])
      .toString(2)
      .replace(/1/g, "#")
      .replace(/0/g, " ");
    return " ".repeat(n - line.length) + line;
  });
}

console.log(solution1(n, arr1, arr2));

const bin1 = (arr1[0] | arr2[0]).toString(2);
console.log(bin1);
