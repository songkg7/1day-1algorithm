# 명령 프롬프트
# 문자열
# 2021/08/13 7:00 오후

N = int(input())
file = [input() for _ in range(N)]

t = list(zip(*file))
result = []

for i in t:
    if len(set(i)) == 1:
        result.extend(set(i))
    else:
        result.append('?')

print(''.join(result))

# ClearTime = 2021/08/13 7:07 오후
