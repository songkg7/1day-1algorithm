# 균현잡힌 세상
# 스택

# TODO: 정리하기

while True:
    string = input()
    if string == ".":
        break

    for s in string:
        if s.isalpha() or s == ' ' or s == '.':
            string = string.replace(s, '')

    stack = []
    for s in string:
        if not stack:
            stack.append(s)
        elif s == ')' and stack[-1] == '(':
            stack.pop()
        elif s == ']' and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(s)

    if not stack:
        print("yes")
    else:
        print("no")
