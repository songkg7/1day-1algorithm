// Clear

let index = 0;
const limit = [10, 15, 150, 30];
let weights = [];

while(index != limit.length) {
    let cnt = 0;
    for (let i = index; i < limit.length; i++) {
      let weight = [];
      console.log(`줄의 갯수 = ${++cnt}`);
      for (let j = index; j <= i; j++) {
        weight.push(limit[j]);
      }
      // 들 수 있는 최대 무게 = 무게 안에서 가장 작은 값 * 무게 배열 갯수
      console.log(`로프들이 각각 견딜 수 있는 무게 : [${weight}]`);
      const answer = Math.min.apply(null, weight) * weight.length;
      weights.push(answer);
      console.log(`병렬로 견딜 수 있는 무게 = ${answer}`);
      console.log("============");
    }
    index++;
}

console.log(`정답 : ${Math.max.apply(null, weights)}`);