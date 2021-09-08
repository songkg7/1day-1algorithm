# 접미사 배열
# 문자열
# 2021/08/13 8:14 오후

s = input()

result = sorted([s[i:] for i in range(len(s))])

for i in result:
    print(i)

# ClearTime = 2021/08/13 8:19 오후
