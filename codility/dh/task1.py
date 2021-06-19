#
#
# 2021/06/19 2:50 오후

import re

S = "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"
C = "Example"


def solution(S, C):
    result = []
    step1 = re.compile(r"(?P<ln>\w+)\s+(?P<fn>\w+)")
    dp = dict()
    peoples = S.split(', ')
    for name in peoples:
        split = name.split(' ')
        name = split[0] + ' ' + split[-1]

        if name in dp:
            dp[name] += 1
        else:
            dp[name] = 1

        if dp[name] == 1:
            p = step1.sub(name + r" <\g<ln>.\g<fn>@" + C.lower() + '.com>',
                          name.lower().replace("-", ''))
        else:
            p = step1.sub(name + r" <\g<ln>.\g<fn>" + str(dp[name]) + '@' + C.lower() + '.com>',
                          name.lower().replace("-", ''))
        result.append(p)

    return result


print(solution(S, C))
