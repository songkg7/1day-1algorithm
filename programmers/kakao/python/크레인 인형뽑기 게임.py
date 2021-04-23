# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    stack = []
    count = 0
    for i in moves:
        for j in range(len(board)):
            # print(board[i][position - 1])
            if board[j][i - 1] != 0:
                stack.append(board[j][i - 1])
                # print(stack)
                # print(f'count = {count}')
                if len(stack) > 1 and stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
                    count += 2

                # print(f'stack last index : {stack[-1]}')
                board[j][i - 1] = 0
                break
    return count


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
# result = 4

print(solution(board, moves))
