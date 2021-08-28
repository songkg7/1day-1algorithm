# TITLE: 찍기
# CATEGORY: 문자열
# DATE: 2021/08/28 10:00 오후

friends = {
    'Adrian': ['A', 'B', 'C'] * 34,
    'Bruno': ['B', 'A', 'B', 'C'] * 25,
    'Goran': ['C', 'C', 'A', 'A', 'B', 'B'] * 17
}

N = int(input())
A = list(input())

result = []
for name in friends:
    count = 0
    answers = friends[name][:N]
    for i in range(N):
        if A[i] == answers[i]:
            count += 1
    result.append((count, name))

result = sorted(result, key=lambda x: (-x[0], x[1]))
best_point = result[0][0]
print(best_point)

for cnt, friend_id in result:
    if cnt == best_point:
        print(friend_id)

# ClearTime = 2021/08/28 10:26 오후
