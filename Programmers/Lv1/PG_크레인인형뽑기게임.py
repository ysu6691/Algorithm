def solution(board, moves):

    answer = 0

    stack = [101]

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break

    return answer