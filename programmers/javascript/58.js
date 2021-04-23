// 위장

const clothes = [
  ["yellow_hat", "headgear"],
  ["blue_sunglasses", "eyewear"],
  ["green_turban", "headgear"],
];

class DirectAddressTable {
  constructor() {
    this.table = [];
  }

  setValue(value = -1) {
    this.table[value] = value;
  }

  getValue(value = -1) {
    return this.table[value];
  }

  getTable() {
    return this.table;
  }
}

const myTable = new DirectAddressTable();
myTable.setValue(3);
myTable.setValue(10);
myTable.setValue(90);

console.log(myTable.getTable());

function solution(clothes) {
  var answer = 1;
  var obj = {};
  for (var i = 0; i < clothes.length; i++) {
    obj[clothes[i][1]] = (obj[clothes[i][1]] || 1) + 1;
  }

  for (var key in obj) {
    answer *= obj[key];
  }

  return answer - 1;
}

console.log(solution(clothes));

// AA

function solution1(clothes) {
  return (
    Object.values(
      clothes.reduce((obj, t) => {
        obj[t[1]] = obj[t[1]] ? obj[t[1]] + 1 : 1;
        return obj;
      }, {})
    ).reduce((a, b) => a * (b + 1), 1) - 1
  );
}

let test = clothes.reduce((obj, t) => {
  obj[t[1]] = obj[t[1]] ? obj[t[1]] + 1 : 1;
  return obj;
}, {});

console.log(test);
