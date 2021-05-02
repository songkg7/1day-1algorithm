# 월간 코드 챌린지 시즌 2
# level 1

absolutes = [4, 7, 12]
signs = [True, False, True]


# result = 9

def solution(absolutes, signs):
    result = [absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes))]
    return sum(result)


print(solution(absolutes, signs))
