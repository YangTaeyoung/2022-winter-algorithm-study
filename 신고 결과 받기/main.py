# 프로그래머스 - 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334


def solution(id_list, report, k):
    id_dict = {id: list() for id in id_list}
    result_dict = {id: 0 for id in id_list}
    report = set(report)
    for rep in report:
        rep_splited = rep.split()
        id_dict[rep_splited[1]].append(rep_splited[0])
    for id in id_dict:
        if len(id_dict[id]) >= k:
            for id in id_dict[id]:
                result_dict[id] += 1
    answer = [result_dict[id] for id in result_dict]
    return answer
