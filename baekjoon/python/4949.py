# 균현잡힌 세상
# 스택

import sys

string = []
while True:
    string.append(sys.stdin.readline().rstrip())
    if string[-1] == '.':
        string.pop()
        break

for j in string:
    stack = []
    for s in j:
        if s in '()[]':
            stack.append(s)

    # print(stack)
    ps = ''.join(stack)

    check = 0

    for i in ps:
        if i == '(':
            check += 2
        elif i == ')':
            check -= 2
        elif i == '[':
            check += 1
        elif i == ']':
            check -= 1

        if check < 0 or check < 0:
            print('no')
            break

    if check == 0 and check == 0:
        print('yes')
    elif check > 0 or check > 0:
        print('no')
