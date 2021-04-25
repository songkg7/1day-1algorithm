from collections import deque

p = ")))(((()"


def detach(string):
    str_que = deque(string)  # queue 활용
    u, v = '', ''
    left = 0
    right = 0
    while str_que:
        u += str_que.popleft()
        if u[-1] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(str_que))
    return u, v


def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack


def reverse(string):
    return ''.join([')' if s == '(' else '(' for s in string])


def recurse(string):
    if string == '':  # 1단계
        return ''

    u, v = detach(string)  # 2단계
    if is_correct(u):  # 3단계
        return u + recurse(v)
    else:  # 4단계
        return '(' + recurse(v) + ')' + reverse(u[1:-1])


def solution(p):
    return p if is_correct(p) else recurse(p)

print(solution(p))