import itertools

def solution(orders, course):
    menu_count_dict = {}
    for order in orders:
        for c in course:
            menu_combinations = itertools.combinations(list(order), c)
            for mc in menu_combinations:
                menu = "".join(mc)
                if menu_count_dict.get("".join(menu)):
                    menu_count_dict[menu] += 1
                else:
                    menu_count_dict[menu] = 1


    print(menu_count_dict)
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])

