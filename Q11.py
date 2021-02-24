# 수학
# 탐욕법, 브루트포스 알고리즘
# 백준 1339번
# NOTE: 완벽하게 스스로 풀지 못했기 때문에 재검토해야함

# words = ["GCF", "ACDEB"]
N = int(input())
words = [input() for _ in range(N)]

dict = {}

for word in words:
    k = len(word)-1
    for s in word:
        # print(s)
        if s in dict:
            dict[s] += pow(10, k)
        else:
            dict[s] = pow(10, k)
        k -= 1

# print(dict["A"])

# values = sorted([value for value in dict.values()], reverse=True)

values = sorted(list(dict.values()), reverse=True)
print(values)

# num, answer = 9, 0
num = 9
answer = 0

for value in values:
    answer += value * num
    num -= 1

print(answer)
