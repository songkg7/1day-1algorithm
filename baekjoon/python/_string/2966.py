# TITLE: 찍기
# CATEGORY: 문자열
# DATE: 2021/08/28 10:00 오후

policies = {
    'Adrian': ['A', 'B', 'C'],
    'Bruno': ['B', 'A', 'B', 'C'],
    'Goran': ['C', 'C', 'A', 'A', 'B', 'B']
}

N = int(input())
A = list(input())

result = []
for policy in policies:
    hit = 0
    for i in range(N):
        answers = policies[policy]
        if A[i] == answers[i % len(answers)]:
            hit += 1
    result.append((hit, policy))

result = sorted(result, key=lambda x: (-x[0], x[1]))
best_point = result[0][0]
print(best_point)  # 가장 많이 맞춘 사람이 맞춘 문제의 수 출력

for point, friend_id in result:
    if point == best_point:
        print(friend_id)  # 가장 많이 맞춘 사람 및 동점자 순서대로 출력

# ClearTime = 2021/08/28 10:26 오후
