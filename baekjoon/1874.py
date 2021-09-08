# 스택 수열
# 스택


# push 되는 숫자는 오름차순으로 stack 에 들어간다.
# 필요한 숫자가 stack 으로 들어오면 pop 을 하고 answer 에 push 한다.
# 비교해야하는 배열 = wanted
# 불가능한 경우 NO 출력

n = int(input())

stack = []
result = []
count = 0
X = True

for _ in range(n):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        X = False
        break

if not X:
    print('NO')
else:
    for i in result:
        print(i)

# 일단 스택에 오름차순으로 숫자를 하나씩 넣는다. -> + 출력
# 넣은 숫자가 wanted 맨 앞에 있는 숫자라면 pop 을 해서 다시 꺼낸다.
# 꺼낸 숫자를 answer 에 넣는다.
# answer 에 들어간 숫자보다 wanted 가장 앞자리의 숫자가 작으면
