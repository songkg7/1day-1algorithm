# 팰린드롬수
# 문자열
# 2021/08/13 9:55 오후

while True:
    s = list(input())

    if s[0] == '0':
        break

    print('yes' if s == s[::-1] else 'no')

# ClearTime = 2021/08/13 10:04 오후
