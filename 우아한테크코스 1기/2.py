# 청개구리
# 우아한 테크코스 1기
# 2021/06/03 10:33 오후

word = input()
answer = []
for s in word:
    # 대문자
    if s.isupper():
        answer.append(chr(90 - ord(s) + 65))
    # 소문자
    elif s.islower():
        answer.append(chr(122 - ord(s) + 97))
    else:
        answer.append(s)

print(''.join(answer))

# ClearTime = 2021/06/03 11:08 오후
