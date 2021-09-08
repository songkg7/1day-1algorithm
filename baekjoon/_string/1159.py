# TITLE: 농구 경기
# CATEGORY: 문자열
# DATE: 2021/08/18 10:48 오후

N = int(input())

players = {}
for _ in range(N):
    name = input()[0]
    players[name] = players.get(name, 0) + 1

answer = sorted(filter(lambda x: players[x] >= 5, players.keys()))
print(''.join(answer) if answer else 'PREDAJA')

# ClearTime = 2021/08/18 11:04 오후
