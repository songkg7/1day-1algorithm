// 실패율

let N = 5;
let stages = [2, 1, 2, 6, 2, 4, 3, 3];
// result =[3,4,2,1,5]

function solution(N, stages) {
  var result = [];
  // N번 스테이지의 실패율
  for (let i = 1; i < N + 1; i++) {
    let arriveStage = stages.filter((v) => v >= i);
    let stillThisStage = arriveStage.filter((v) => v <= i);
    let failpct = stillThisStage.length / arriveStage.length;
    result.push({ index: i, ratio: failpct });
  }

  result.sort((a, b) => b.ratio - a.ratio);
  return result.map((val) => val.index);
}

console.log(solution(N, stages));

// AA
function solution1(N, stages) {
  var answer = [];
  var stack = [];
  let users = stages.length;
  // [] {stage, 실패율}
  for (var i = 1; i <= N; i++) {
    const len = stages.filter((value) => value === i).length; // stage i 에 있는 사람의 수
    if (len === 0) {
      stack.push({ index: i, ratio: 0 });
    } else {
      stack.push({ index: i, ratio: len / users }); // 실패율을 push
      users -= len; // 첫 스테이지 이후에는 그만큼 제외
    }
  }

  stack.sort((a, b) => {
    if (b.ratio === a.ratio) {
      // a와 b의 실패율이 같다면 오름차순으로 정렬
      return a.index - b.index;
    } else {
      return b.ratio - a.ratio;
    }
  });
  return stack.map((value) => value.index); // index: ratio 에서 index만 추출
}

console.log(solution1(N, stages));
