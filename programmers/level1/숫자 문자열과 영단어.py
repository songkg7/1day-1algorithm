#
# 2021 kakao 채용연계형 인턴십
# 2021/07/15 7:56 오후

s = "one4seveneight"


def solution(s):
    data = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    for k, v in data.items():
        # replace 는 바꾸고자하는 문자가 존재하지 않는다면 무시된다.
        s = s.replace(k, str(v))
    return int(s)


print(solution(s))

# ClearTime = 2021/07/15 8:06 오후
