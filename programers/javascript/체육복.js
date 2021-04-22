var lost = [3];
var reserve = [1];
// return = 5

function solution(n, lost, reserve) {
  const answer = [];
  let students = [];
  for (let i = 1; i <= n; i++) {
    students.push(1); // n명만큼 students에 1 추가
    if (reserve.includes(i)) {
      students[i - 1]++; // 여벌의 체육복을 가지고 잇다면 그 학생에게 1을 추가
    }
    if (lost.includes(i)) {
      students[i - 1]--; // 도난당한 학생이라면 그 학생의 체육복을 1개 감소
    }
  }
  //   return students;
  for (let i = 0; i < n; i++) {
    if (!students[i]) {
      if (students[i - 1] === 2) {
        students[i]++;
        students[i - 1]--;
      } else if (students[i + 1] === 2) {
        students[i]++;
        students[i + 1]--;
      }
    }
  }

  for (let i = 0; i < n; i++) {
    if (students[i] > 0) {
      answer.push(1);
    }
  }
  console.log(students);
  return answer.length;
}

console.log(solution(5, lost, reserve));
