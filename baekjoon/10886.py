# TITLE: 0 = not cute / 1 = cute
# CATEGORY: math
# DATE: 2021/09/29 8:22 오후

N = int(input())
count = 0
for _ in range(N):
    result = int(input())
    if result == 1:
        count += 1
    else:
        count -= 1

print("Junhee is cute!" if count > 0 else "Junhee is not cute!")

# ClearTime = 2021/09/29 8:27 오후
