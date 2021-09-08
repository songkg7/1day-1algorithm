# TITLE: 오타맨 고창영
# CATEGORY: 문자열
# DATE: 2021/08/26 4:48 오후

T = int(input())
for _ in range(T):
    _list = input().split()
    idx = int(_list[0])
    word = _list[1]

    word = word[:idx - 1] + word[idx:]

    print(word)

# ClearTime = 2021/08/26 4:55 오후
