# 다이얼
# 문자열

# 직관적이게 푸는 방법 ㅋㅋ..
# dial 을 배열에 담아놓고 인덱스 값을 가져와서 계산하는 것도 괜찮을듯

words = input()

time = 0
for s in words:
    if s in "ABC":
        time += 3
    elif s in "DEF":
        time += 4
    elif s in "GHI":
        time += 5
    elif s in "JKL":
        time += 6
    elif s in "MNO":
        time += 7
    elif s in "PQRS":
        time += 8
    elif s in "TUV":
        time += 9
    elif s in "WXYZ":
        time += 10

print(time)
