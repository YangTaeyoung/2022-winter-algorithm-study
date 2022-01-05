# 프로그래머스 - 크래인 인형뽑기 게임 문제 풀이
# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board: list, moves: list):
    # 바구니에 담겨있는 인형 스텍
    bucket_stack = []
    # 사라진 인형 개수를 담는 변수
    answer = 0
    for move in moves:
        for i in range(len(board)):
            crain_hold = board[i][move - 1]
            # 크래인이 잡고 있는 것이 있는 경우
            if crain_hold != 0:
                board[i][move - 1] = 0
                if len(bucket_stack) == 0 or crain_hold != bucket_stack[-1]:
                    bucket_stack.append(crain_hold)
                    break
                else:
                    bucket_stack.pop(-1)
                    # pop는 한번 호출되나 크래인이 잡고 있는 인형과 바구니에 있던 인형 2개가 사라지므로, 해당 단계에 +2씩 해준다.
                    answer += 2
                    break
    return answer
