# 프로그래머스 실패율 문제 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N: int, stages: list):
    fail_counts = [0 for i in range(0, N + 1)]
    for stage in stages:
        fail_counts[stage - 1] += 1
    fail_rates = {}
    for i in range(len(fail_counts) - 1):
        if total := sum(fail_counts[i:]):
            fail_rates[i] = fail_counts[i] / total
        else:
            fail_rates[i] = 0
    sorted_list = sorted(fail_rates.items(), key=lambda item: item[1], reverse=True)
    answer = [item[0] + 1 for item in sorted_list]
    return answer
