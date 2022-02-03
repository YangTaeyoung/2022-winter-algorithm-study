# 프로그래머스 - 양궁대회
# https://programmers.co.kr/learn/courses/30/lessons/92342
# 이번건 좀 어려웠다
candidates = list()


def is_finish(node_idx: int, rest_n: int, apeachs):
    if rest_n > 0:
        for i in range(node_idx + 1, 11):
            if apeachs[i] <= rest_n:
                return False
        return True
    return False


def dfs(node_idx, apeachs, lions, rest_n, visited):
    visited_copied = visited.copy()
    visited_copied[node_idx] = True
    lions_copied = lions.copy()

    if rest_n >= (l_point := apeachs[node_idx] + 1):
        lions_copied[node_idx] = apeachs[node_idx] + 1
        rest_n -= l_point

    if is_finish(node_idx, rest_n, apeachs):
        lions_copied[-1] = rest_n
        rest_n = 0

    if not rest_n:  # 남은 화살이 없는 경우
        if lions[-1] == 2:
            print(lions)
        if (diff := get_diff(apeachs, lions_copied)) > 0:  # 라이언이 이기는 경우
            candidates.append((lions_copied, diff))  # (점수 리스트, 점수 차이) 튜플을 후보군에 삽입
        return

    for i in range(node_idx + 1, 11):
        if not visited_copied[i]:
            dfs(i, apeachs, lions_copied, rest_n, visited)


def get_diff(apeachs, lions):
    apeach_point = 0
    lion_point = 0
    for i in range(11):
        a_point = apeachs[i]
        l_point = lions[i]
        if not apeachs[i] and not lions[i]:
            continue
        if a_point >= l_point:
            apeach_point += 10 - i
        else:
            lion_point += 10 - i
    return lion_point - apeach_point


def solution(n: int, info: list):
    for i in range(11):
        lions = [0] * 11
        visited = [False] * 11
        dfs(i, info, lions, n, visited)
    if candidates:
        candidates.sort(reverse=True, key=lambda x: x[0][::-1])

        return max(candidates, key=lambda x: x[1])[0]
    else:
        return [-1]
