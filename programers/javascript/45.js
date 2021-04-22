// 다리를 지나는 트럭

const bridge_length = 100;
const weight = 100;
const truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10];
// return = 8

function solution(bridge_length, weight, truck_weights) {
  var answer = 0; // 걸린 시간
  var queue = []; // 현재 다리 상태
  var queueSum = 0; // 현재 다리 무게

  // queue 의 길이는 다리의 길이
  for (let i = 0; i < bridge_length; i++) {
    queue.push(0);
  }

  // 다리에 트럭 추가
  let now_truck = truck_weights.shift();
  queue.unshift(now_truck);
  queue.pop();

  // 다리 무게증가
  queueSum += now_truck;

  // 시간 증가
  answer++;

  // 쉬지 않고 건너기 때문에 queueSum이 0이 되면 모두 지나간 것
  while (queueSum) {
    //다리에 있는 트럭 이동
    queueSum -= queue.pop();

    // 다리를 안건넌 트럭 하나 빼고,
    now_truck = truck_weights.shift();

    // 다리에 들어갈 수 있으면 큐(다리)에 넣고 무게 증가
    if (now_truck + queueSum <= weight) {
      queue.unshift(now_truck);
      queueSum += now_truck;
    }
    // 다리에 들어갈 수 없으면 다시 트럭 집단에 그대로 넣어줌
    else {
      queue.unshift(0);
      truck_weights.unshift(now_truck);
    }
    answer++;
  }
  return answer;
}

// console.log(now_truck);
// console.log(truck_weights);
console.log(solution(bridge_length, weight, truck_weights));
