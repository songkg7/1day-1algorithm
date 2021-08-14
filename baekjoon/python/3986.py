# 좋은 단어
# 문자열
# 2021/08/14 2:20 오전

# 괄호 문제와 같다. 문제의 설명이 부족한 느낌이 들어 아쉬운 부분.

N = int(input())
words = [input() for _ in range(N)]

count = 0
for word in words:
    stack = []
    for i in range(len(word)):
        if stack and stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])

    if not stack:
        count += 1

print(count)

# ClearTime = 2021/08/14 2:52 오전
