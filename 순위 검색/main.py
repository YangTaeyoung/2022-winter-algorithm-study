# 프로그래머스 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412


# 첫번째 시도, 효율성 테스트 실패. 자료구조를 사용해야 할듯 젠장
# 앞으로 효율성 테스트가 있을 때는 꼭 효율적인 자료구조를 사용해야 할 듯ㅠ
# def pre_process(li: list):
#     return [el.replace("and", "").split() for el in li]
#
#
# def list_remove(li: list, el):
#     try:
#         li.remove(el)
#     except ValueError:
#         return


# def solution(info: list, query: list):
#     databases = pre_process(info)
#     processed_queries = pre_process(query)
#     answer = []
#
#     for processed_query in processed_queries:
#         index_list = list(range(len(databases)))
#         for i, data in enumerate(databases):
#             for el_query, el_data in zip(processed_query, data):
#                 if el_query.isdigit():
#                     if int(el_query) > int(el_data):
#                         list_remove(index_list, i)
#                         break
#                 else:
#                     if el_query != "-" and el_query != el_data:
#                         list_remove(index_list, i)
#                         break
#         answer.append(len(index_list))
#     return answer

# 두 번째 시도 - 딕셔너리 사용 - 시간초과
# def solution(info, query):
#     databases = dict()
#     databases["digit"] = list()
#     for i, record in enumerate(info):
#         for r in record.split():
#             if r.isdigit():
#                 databases["digit"].append((i, int(r)))
#             if not databases.get(r):
#                 databases[r] = set()
#                 databases[r].add(i)
#             else:
#                 databases[r].add(i)
#     answer = list()
#     for qq in query:
#         result = set(range(len(info)))
#         for q in qq.replace("and", "").split():
#             if q.isdigit():
#                 result &= {record[0] for record in databases["digit"] if record[1] >= int(q)}
#             elif q != "-":
#                 result &= databases[q]
#         answer.append(len(result))
#     return answer

# 세번째 시도 - 판다스 사용
# 판다스도 안될 건 안된다. 오히려 3개 방법중 가장 늦었음...
# import pandas as pd
#
#
# def solution(info, query):
#     databases = {
#         "개발언어": list(), "직군": list(), "경력": list(), "소울푸드": list(), "점수": list()
#     }
#     for record in info:
#         for col_name, el in zip(databases.keys(), record.split()):
#             if col_name == "점수":
#                 el = int(el)
#             databases[col_name].append(el)
#     df = pd.DataFrame(databases)
#     answer = list()
#     for qq in query:
#         result = df
#         for q, col_name in zip(qq.replace("and", "").split(), databases.keys()):
#             if col_name == "점수" and q != "-":
#                 result = result[result[col_name] >= int(q)]
#             elif q != "-":
#                 result = result[result[col_name] == q]
#         answer.append(len(result.index))
#     return answer

from itertools import combinations
from collections import defaultdict


# 네번째 시도 - 조합 사용
def solution(infos, queries):
    # defaultdict: 키가 생성될 때 value에 지정된 형식의 자료구조를 미리 만들 수 있음.
    db = defaultdict(list)
    answer = list()
    for info in infos:
        record = info.split()
        db_key = record[:-1]
        db_value = int(record[-1])
        for i in range(5):
            for combi in list(combinations(db_key, i)):
                db[''.join(combi)].append(db_value)

    for key in db.keys():
        db[key].sort()

    for query in queries:
        query = query.replace("and", "").replace("-", "").split()
        query_key = ''.join(query[:-1])
        query_value = int(query[-1])
        if target_scores := db[query_key]:
            left, right = 0, len(target_scores)
            # 이진 탐색을 통해 경계선 찾기
            while left < right:
                mid = (left+right) // 2
                if target_scores[mid] >= query_value:
                    right = mid
                else:
                    left = mid+1
            answer.append(len(target_scores)-left)
        else:
            answer.append(0)
    return answer

print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
