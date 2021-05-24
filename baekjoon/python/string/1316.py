# 그룹 단어 체커
# 문자열

# TODO: 정리하기

T = int(input())
count = 0
for _ in range(T):
    stack = []
    word = input()
    is_group = True

    for s in word:
        if s not in stack or not stack:
            stack.append(s)
        elif s in stack and stack[-1] != s:
            is_group = False

    if is_group:
        count += 1

print(count)
