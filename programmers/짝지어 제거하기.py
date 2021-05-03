# 2017 팁스타운
# level 2

# TODO: 다시 풀어보기

s = "aaabbabaab"


def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution(s))
