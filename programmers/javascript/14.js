// 카카오 개발자 겨울 인턴십 크레인 인형뽑기 게임

let board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];

let moves = [1, 5, 3, 5, 1, 2, 1, 4];

// function solution(board, moves) {
//   let stack = [];
//   let choicesCount = 0;
//   let point = 0;
//   // moves[0]부터 board[i][0] 와 비교해나간다
//   for (let i = 0; i < moves.length; i++) {
//     for (let j = 0; j < board.length; j++) {
//       if (board[j][moves[i] - 1] !== 0 && choicesCount === i) {
//         choicesCount++; // 한 위치에서 계속 인형을 집어오는 것을 방지하기 위해 choicesCount를 추가
//         if (stack[stack.length - 1] === board[j][moves[i] - 1]) {
//           stack.pop(); // 뽑아온 인형을 담아놓은 곳의 마지막 인형과 비교 후 같으면 삭제
//           point += 2;
//         } else stack.push(board[j][moves[i] - 1]); // 인형을 옮긴다
//         board[j][moves[i] - 1] = 0; // 인형을 옮겨서 빈 칸이 되었으므로 0 으로 바꾼다
//       }
//     }
//   }
//   return point;
// }

// console.log(solution(board, moves));

// 다른 풀이법
function solution1(board, moves) {
  let stack = [];
  let point = 0;
  // moves[0]부터 board[i][0] 와 비교해나간다
  for (let i = 0; i < moves.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1] !== 0) {
        if (stack[stack.length - 1] === board[j][moves[i] - 1]) {
          stack.pop(); // 뽑아온 인형을 담아놓은 곳의 마지막 인형과 비교 후 같으면 삭제
          point += 2;
        } else stack.push(board[j][moves[i] - 1]);
        // 인형을 옮긴다
        board[j][moves[i] - 1] = 0; // 인형을 옮겨서 빈 칸이 되었으므로 0 으로 바꾼다
        break;
      }
    }
  }
  return point;
}

console.log(solution1(board, moves));
