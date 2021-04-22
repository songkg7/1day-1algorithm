// 직사각형 별찍기

function solution(a, b) {
  return Array(b)
    .fill()
    .map(() => "*".repeat(a))
    .join("\n");
}
