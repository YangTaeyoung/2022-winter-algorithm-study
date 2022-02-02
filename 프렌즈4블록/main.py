# 프로그래머스 - 프렌즈4 블록 문제
# https://programmers.co.kr/learn/courses/30/lessons/17679


# 리스트를 순회하여 블록을 재구조화 함 (부숴진 블록(#)을 찾아위로 올림)
# 움직인 횟수 반환
def restructuring(m, n, board: list):
    move_count = 0
    for _ in range(m):
        for y in range(m):
            for x in range(n):
                if (y_check := y + 1) < m:
                    if board[y_check][x] == '#' and board[y][x] != '#':
                        board[y_check][x], board[y][x] = board[y][x], board[y_check][x]
                        move_count += 1
    return move_count


# 빈칸 개수를 새는 함수
def count_blank(board: list):
    cnt = 0
    for row in board:
        cnt += row.count('#')
    return cnt


def solution(m: int, n: int, board: list):
    board = [list(row) for row in board]
    dis = [
        [0, 1, 1],
        [1, 0, 1]
    ]
    while True:
        # 빈칸으로 박살날 후보들 모임
        result_founded = set()
        for y in range(m):
            for x in range(n):
                # 빈칸(#)인 경우 해당 좌표는 보지 않고 넘어감
                if board[y][x] == "#":
                    continue
                cur_block = board[y][x]
                founded_blocks = list()  # 현재 좌표로부터 4블록 감지하는 임시 리스트
                founded_blocks.append((x, y))  # 현재 좌표 삽입
                for i in range(3):  # 2*2 가 있는 블록들 좌표
                    if (y_check := y + dis[1][i]) < m and (x_check := x + dis[0][i]) < n and board[y_check][x_check] == cur_block:
                        founded_blocks.append((x_check, y_check))  # 조건에 맞는 좌표 삽입
                if len(founded_blocks) == 4:  # 4블록 발견시
                    for point in founded_blocks:  # 임시리스트에 있는 좌표를 결과 리스트로 보냄
                        result_founded.add(point)

        # 결과 리스트에 있는 모든 좌표를 #으로 바꿈(4블록 감지 후니까)
        for result in result_founded:
            board[result[1]][result[0]] = '#'

        # 재구조화로 인해 변경된 블록이 0개인 경우 (즉 다시 돌려도 이전과 결과가 같은 경우)
        if restructuring(m, n, board) == 0:
            # 프로그램 종료
            break

    return count_blank(board)


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
