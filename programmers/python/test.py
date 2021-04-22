a, b = map(int, input().split())


print(a*(b%10),a*((b//10)%10),a*(b//100),a*b)