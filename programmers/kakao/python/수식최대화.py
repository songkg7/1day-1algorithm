# 2020 카카오 인턴십
# level 2

from itertools import permutations
import re

exp = "100-200*300-500+20"


# result = 60420

def solution(expression):
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)
    cand = []

    for op_cand in prior:
        temp = re.compile("(\D)").split(expression)
        print(temp)
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx - 1] + [str(eval(''.join(temp[idx - 1:idx + 2])))] + temp[idx + 2:]
                print(temp)
        cand.append(abs(int(temp[0])))
    return max(cand)


print(solution(exp))
