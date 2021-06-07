# 2017 팁스타운
# level 2

def solution(s):
    stack = []
    for word in s:
        if len(stack) > 0 and word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)

    if stack:
        return 0
    else:
        return 1

# ClearTime = 2021/06/07 5:50 오후
