# TITLE: 세로읽기
# CATEGORY: 문자열
# DATE: 2021/08/17 2:57 오후

# zip 은 길이가 더 짧은 배열을 우선시하여 남는 부분은 무시된다.
# 글자 수의 제한이 15개이므로 미리 초기화하는 방법을 사용

words = []
for _ in range(5):
    s = list(input())
    s = s + ([''] * (15 - len(s)))
    words.append(s)

for w in zip(*words):
    print(''.join(w), end='')

# ClearTime = 2021/08/17 3:09 오후
