# 크로아티아 알파벳
# 문자열

# TODO: 정리하기

croatia_alphas = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for al in croatia_alphas:
    word = word.replace(al, "*")

print(len(word))
