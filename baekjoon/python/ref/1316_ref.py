# 정렬시 key 설정을 자세히 살펴보자
# 코드를 상당히 줄일 수 있다.

N = int(input())
count = 0
for i in range(N):
    a = input()
    if list(a) == sorted(a, key=a.find):
        count += 1
print(count)
