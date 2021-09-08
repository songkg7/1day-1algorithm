# TITLE: ROT13
# CATEGORY: String
# DATE: 2021/08/17 4:31 오후

word = list(input())
for i in range(len(word)):
    if word[i].isupper():
        if ord(word[i]) + 13 <= 90:
            word[i] = chr(ord(word[i]) + 13)
        else:
            word[i] = chr(ord(word[i]) + 13 - 26)
    if word[i].islower():
        if ord(word[i]) + 13 <= 122:
            word[i] = chr(ord(word[i]) + 13)
        else:
            word[i] = chr(ord(word[i]) + 13 - 26)

print(''.join(word))

# ClearTime = 2021/08/17 4:53 오후
