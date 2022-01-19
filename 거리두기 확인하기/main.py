# 프로그래머스 - 거리두기 확인하기 문제
# https://programmers.co.kr/learn/courses/30/lessons/81302

# 거리 계산 함수
def get_distance(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# 거리가 2이하일 때 파티션이 중간에 존재하는지 확인하는 함수
def is_partition(place: list, p1: tuple, p2: tuple):
    # 일직선 상에 두 좌표가 있는 경우
    if p1[0] == p2[0]:
        if place[(p1[1] + p2[1]) // 2][p1[0]] == "X":
            return True
    elif p1[1] == p2[1]:
        if place[p1[1]][(p1[0] + p2[0]) // 2] == "X":
            return True
    # 대각선 관계에서 두 좌표가 있는 경우
    else:
        return diagonal_check(place, p1, p2)


# 두 좌표가 대각선상에 존재할 때 사이에 파티션이 존재하는지 확인하는 함수
def diagonal_check(place: list, p1, p2):
    # 케이스 정규화 (x기준)
    # 더 낮은 x좌표를 가진 사람을 p1으로 설정
    if p1[0] > p2[0]:
        p1, p2 = p2, p1

    # 케이스 패턴별 파티션 체크
    # 케이스 1 정방향
    if p1[1] < p2[1]:
        if place[p1[1]][p2[0]] == "X" and place[p2[1]][p1[0]] == "X":
            return True
    # 케이스 2 역방향
    else:
        if place[p2[1]][p1[0]] == "X" and place[p1[1]][p2[0]] == "X":
            return True
    return False


def check_distance(place: list):
    # 사람들이 있는 좌표 리스트
    P_list = [(x, y) for y in range(len(place)) for x in range(len(place[y])) if place[y][x] == "P"]

    for p1 in P_list:
        for p2 in P_list:
            if p1 == p2:
                continue
            if get_distance(p1, p2) <= 2:
                if not is_partition(place, p1, p2):
                    return 0
    return 1


def solution(places):
    return [check_distance(place) for place in places]


print(check_distance(
    [
        "POPOP",
        "XPXPX",
        "PXPXP",
        "XPXPX",
        "PXPXP"
    ]
))
