// H-Index

const citations = [3, 0, 6, 1, 5];
// return = 3;

function solution(citations) {
  citations.sort((a, b) => b - a);

  console.log(citations);
  var index = 0;
  while (index <= citations.length) {
    if (index + 1 <= citations[index]) {
      index++;
    } else break;
  }
  return index;
}

console.log(solution(citations));

/* 문제이해를 잘못했었다. h개 이상과 h개 이하일 때의 남은 값이 같아야한다고 생각했다.
 */
