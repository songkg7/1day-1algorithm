import sys

rgb = [0, 0, 0]
for _ in range(int(sys.stdin.readline().strip())):
    r, g, b = map(int, sys.stdin.readline().strip().split())
    r += min(rgb[1], rgb[2])
    g += min(rgb[0], rgb[2])
    b += min(rgb[0], rgb[1])
    rgb = [r, g, b]
print(min(rgb))
