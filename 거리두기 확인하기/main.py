def get_distance(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def is_partition(place: list, p1: tuple, p2: tuple):
    if p1[0] == p2[0]:
        if place[(p1[1] + p2[1]) // 2][p1[0]] == "X":
            return True
    elif p1[1] == p2[1]:
        if place[p1[1]][(p1[0] + p2[0]) // 2] == "X":
            return True
    else:
        return diagonal_check(place, p1, p2)


def diagonal_check(place: list, p1, p2):
    # 케이스 정규화 (x기준)
    if p1[0] > p2[0]:
        p1, p2 = p2, p1

    # 케이스 패턴별 파티션 체크
    # 케이스 1 정방향
    if p1[1] + 1 == p2[1]:
        if place[p1[1]][p2[0]] == "X" and place[p2[1]][p1[0]] == "X":
            return True
    # 케이스 2 역방향
    else:
        if place[p2[1]][p1[0]] == "X" and place[p1[1]][p2[0]] == "X":
            return True
    return False


# 케이스 2 역방향

def check_distance(place: list):
    P_list = list()
    for y in range(len(place)):
        for x in range(len(place[y])):
            if place[y][x] == "P":
                P_list.append((x, y))
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
