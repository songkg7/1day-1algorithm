# 열개씩 끊어 출력하기
# 문자열
# 2021/08/13 5:57 오후

s = input()

for i in range(10, len(s)+10, 10):
    print(s[i-10:i])

# ClearTime = 2021/08/13 6:03 오후
