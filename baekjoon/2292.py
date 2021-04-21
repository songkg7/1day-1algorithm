# 벌집

# [1], [2, ...7], [8, ...19],
# 1 7 19 37 61 ...
# +6 +12 +18 +24
# +6*1, +6*2, +6*3, +6*4
# 58

N = int(input())
x = 1
count = 1
while x < N:
    x += 6 * count
    count += 1

print(count)
