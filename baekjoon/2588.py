# 백준
# 2588번
# 곱셈

a = int(input())
b = int(input())

x = list(map(int, str(b)))

print(a * x[2])
print(a * x[1])
print(a * x[0])
print(a * b)

# 나머지를 이용하여 풀어도 된다.
# 375를 100 으로 나누면 몫은 3 나머지는 75 == 몫은 100의 자릿수
# 10으로 나누면 나머지는 5 == 나머지는 1의 자릿수
# print(b % 10)

