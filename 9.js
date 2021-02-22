// Clear

let index = 0;
let limit = [10, 15, 50];
let weights = [];

while(index != limit.length) {
    let sum = 0;
    let cnt = 0;
    for (let i = index; i < limit.length; i++) {
      let weight = [];
      console.log(`줄의 갯수 = ${++cnt}`);
      for (let j = index; j <= i; j++) {
        // console.log(limit[j]);
        // weight += limit[j];
        weight.push(limit[j]);
      }
      // 들 수 있는 최대 무게 = 무게 안에서 가장 작은 값 * 무게 배열 갯수
      console.log(`선택한 로프들이 견딜 수 있는 무게 : [${weight}]`);
      let answer = Math.min.apply(null, weight) * weight.length;
      weights.push(answer);
      console.log(`줄이 견딜 수 있는 무게 = ${answer}`);
      console.log("============");
    }
    index++;
}

console.log(`정답 : ${Math.max.apply(null, weights)}`);