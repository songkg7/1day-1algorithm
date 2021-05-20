# 단어 정렬
# 정렬

N = int(input())
words = sorted(set(input() for _ in range(N)), key=lambda x: (len(x), x))

for word in words:
    print(word)
