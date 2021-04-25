# 2020 kakao blind recruitment

from collections import deque


def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        # 배열이 비어있지 않으면 True, stack 에 '(' 가 최소 1개는 있을 것이므로, 마지막 '('를 없앤다.
        elif stack:
            stack.pop()
    # 배열이 비어있으면 True 를 리턴해준다.
    return not stack


def detach(string):  # u, v 로 분리
    str_que = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while str_que:
        u += str_que.popleft()
        if u[-1] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break  # 균형 잡힌 괄호

    v = ''.join(list(str_que))
    return u, v


def reverse(u):  # 뒤집기
    return ''.join([')' if s == '(' else '(' for s in u])


def recursive(string):
    if string == '':  # 1단계
        return ''
    u, v = detach(string)  # 2단계
    if is_correct(u):  # 3단계
        return u + recursive(v)
    else:  # 4단계
        return '(' + recursive(v) + ')' + reverse(u[1:-1])


# print(detach(")))((())"))

def solution(p):
    return p if is_correct(p) else recursive(p)


