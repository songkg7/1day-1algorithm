# 문자열 폭발
# 문자열
# 2021/08/13 11:55 오후

# TODO: 다시 풀기

def main():
    s = input()
    bomb = input()

    last_char = bomb[-1]
    stack = []
    length = len(bomb)

    for char in s:
        stack.append(char)
        if char == last_char and ''.join(stack[-length:]) == bomb:  # 폭발 문자열 발견!
            del stack[-length:]

    answer = ''.join(stack)

    if answer:
        print(answer)
    else:
        print('FRULA')


if __name__ == '__main__':
    main()
