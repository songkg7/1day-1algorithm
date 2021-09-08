# 알파벳 찾기
# 문자열

# a~z 까지의 아스키코드 숫자로 범위를 지정해놓고 변환해서 풀어도 된다.
from string import ascii_lowercase

S = input()

alphas = [*ascii_lowercase]

# for al in alphas:
#     if al in S:
#         print(S.index(al), end=' ')
#     else:
#         print(-1, end=' ')

for al in alphas:
    print(S.find(al), end=' ')
