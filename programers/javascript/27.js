// 핸드폰 번호 가리기
const phone_number = "01032164597";

function solution(phone_number) {
  return phone_number.replace(/\d(?=\d{4})/g, "*");
}
// 정규식 ?= 은 뒤에서부터 찾는 명령어

console.log(solution(phone_number));
