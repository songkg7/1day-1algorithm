# 직사각형에서 탈출
# 기본수학 2

x, y, w, h = map(int, input().split())

# w - x, y - h 중 작은 절대값
# 0, 0 이 왼쪽 아래이므로 0 하고도 비교

pos1 = abs(w - x)
pos2 = abs(y - h)
pos3 = abs(0 - x)
pos4 = abs(0 - y)

distance = [pos1, pos2, pos3, pos4]
print(min(distance))
