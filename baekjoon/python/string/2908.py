# 상수
# 문자열

# NOTE: [::-1] 를 사용하면 쉽게 뒤집을 수 있다.

words = input().split()

for i in range(len(words)):
    w = ''
    for s in list(words[i]).__reversed__():
        w += s
    words[i] = w
print(max(list(map(int, words))))

