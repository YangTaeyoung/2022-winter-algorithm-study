# 프로그래머스 - 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411


import itertools
import collections


def solution(orders, course):
    menu_count_dict = {}
    for order in orders:
        keyword = list(order)
        keyword.sort()
        order = "".join(keyword)
        for c in course:
            menu_combinations = itertools.combinations(list(order), c)
            for mc in menu_combinations:
                menu = "".join(mc)
                if menu_count_dict.get("".join(menu)):
                    menu_count_dict[menu] += 1
                else:
                    menu_count_dict[menu] = 1
    len_dict = dict()
    for c in course:
        len_dict[c] = list()
    for menu_count in menu_count_dict:
        len_dict[len(menu_count)].append((menu_count, menu_count_dict[menu_count]))
    answer = []
    for c in course:
        m = max(len_dict[c], key=lambda x: x[1])[1]
        if m >= 2:
            answer += [menu[0] for menu in len_dict[c] if menu[1] == m]
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))


# 개인적으로 생각하는 짠 코드중 가장 비효율 적인 코드
# 다른 사람의 풀이를 보니 collection.Counter 를 사용한 예시가 있는데 좋아 보여서 붙여 놓음.


def solution_2(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]
