import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    ps = input()
    ps = ps[:-1]
    while "()" in ps:
        ps = ps.replace("()", "")
    if ps:
        print("NO")
    else:
        print("YES")