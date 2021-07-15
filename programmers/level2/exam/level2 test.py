#
#
# 2021/07/15 6:52 오후

s = "1 2 3 4"

def solution(s):
    t = list(map(int, s.split()))
    answer = map(str, [min(t), max(t)])
    result = " ".join(answer)
    return result


print(solution(s))

# ClearTime = 2021/07/15 6:59 오후
