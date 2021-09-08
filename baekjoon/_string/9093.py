# TITLE: 단어 뒤집기
# CATEGORY: 문자열
# DATE: 2021/08/18 10:26 오후

T = int(input())
for _ in range(T):
    strings = input().split()
    new_str = []
    for w in strings:
        new_str.append(w[::-1])

    print(' '.join(new_str))

# ClearTime = 2021/08/18 10:32 오후
