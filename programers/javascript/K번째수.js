array = [1, 5, 2, 6, 3, 7, 4];
commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
  [3, 4, 1],
];

console.log(array.slice(2 - 1, 5).sort()[3 - 1]);
// return = [5,6,3]
function solution(array, commands) {
  var answer = [];
  for (let a = 0; a < commands.length; a++) {
    var i = commands[a][0];
    var j = commands[a][1];
    var k = commands[a][2];

    const value = array.slice(i - 1, j).sort((a, b) => {
      return a - b;
    });
    answer.push(value[k - 1]);
  }
  return answer;
}

console.log(solution(array, commands));
