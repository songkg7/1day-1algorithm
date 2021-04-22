// Skill Trees

const skill = "CBD";
const skill_trees = ["BACDE", "CBADF", "AECB", "BDA"];
function solution(skill, skill_trees) {
  var answer = 0;

  skill_trees.forEach((item) => {
    var skill_temp = skill.split("");
    answer++;
    console.log(answer);
    for (var i of item) {
      //   console.log(item);
      console.log(i);
      if (skill_temp.includes(i)) {
        if (skill_temp.indexOf(i) === 0) {
          skill_temp.shift();
        } else {
          answer--;
          break; // skill_trees의 중간에 skill 순서에 맞지 않는 원소가 등장하면 다음 trees 실행
        }
      }
    }
  });
  return answer;
}

console.log(solution(skill, skill_trees));

// AA

function solution1(skill, skill_trees) {
  var answer = 0;
  var regex = new RegExp(`[^${skill}]`, "g");

  return skill_trees
    .map((x) => x.replace(regex, ""))
    .filter((x) => {
      return skill.indexOf(x) === 0 || x === "";
    }).length;
}
