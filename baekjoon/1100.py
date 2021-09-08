# 하얀 칸
# 문자열
# 2021/08/13 6:37 오후

count = 0
for _ in range(4):
    line1 = input()
    line2 = input()

    for i in range(0, len(line1), 2):
        if line1[i] == 'F':
            count += 1

    for i in range(1, len(line2), 2):
        if line2[i] == 'F':
            count += 1

print(count)

# ClearTime = 2021/08/13 6:46 오후
