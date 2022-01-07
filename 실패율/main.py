# 프로그래머스 실패율 문제 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N: int, stages: list):
    # 실패한 사람 수를 리스트에 각 스테이지 마다 담음
    fail_counts = [0 for _ in range(0, N + 1)]
    fail_counts = [fail_counts[stage - 1] += 1 for stage in stages]
    # 실패율을 계산하여 스테이지는 키, 실패율은 값에 담음
    fail_rates = { i : fail_counts[i] / total 
              if (total := sum(fail_counts[i:])) else 0
              for i in range(len(fail_counts) - 1) 
             }
    # 정렬하여 키값(스테이지)만 리스트에 담아 반환
    return [item[0] + 1 for item in sorted(fail_rates.items(), key=lambda item: item[1], reverse=True)]
