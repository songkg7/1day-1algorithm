# 암호문
# 우아한 테크코스
# 2021/06/03 11:42 오후

from collections import deque

cryptogram = input()


def duplicate(word):
    arr = deque(word)
    stack = deque()
    count = 0
    while arr:
        s = arr.popleft()
        if not stack:
            stack.append(s)
        elif s == stack[-1]:
            stack.pop()
            count += 1
        else:
            stack.append(s)

    if count == 0:
        return ''.join(stack)
    else:
        return duplicate(stack)


print(duplicate(cryptogram))

# ClearTime = 2021/06/03 11:55 오후
