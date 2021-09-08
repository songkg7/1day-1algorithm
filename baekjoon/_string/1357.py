# TITLE: 뒤집힌 덧셈
# CATEGORY: 문자열
# DATE: 2021/08/18 10:41 오후

X, Y = map(int, input().split())


def rev(num):
    return int(str(num)[::-1])


print(rev(rev(X) + rev(Y)))

# ClearTime = 2021/08/18 10:47 오후
