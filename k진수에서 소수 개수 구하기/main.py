# 프로그래머스 - k진수에서 소수 개수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/92335


import math


# 소수인지 판별
def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# num을 digit진수로 변환
def get_n_digit(num: int, digit: int):
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    mok = num
    result = list()
    while True:
        reminder = mok % digit  # 나머지임
        mok //= digit  # 몫임
        result.append(num_list[reminder])  # 나머지를 붙일거임
        if mok < digit:
            if mok:
                result.append(num_list[mok])  # 마지막은 몫을 붙일거임
            break
    result.reverse()  # 뒤집을거임
    return "".join(result)  # ㅋㅋㄹㅃㅃ


def solution(n, k):
    answer = 0
    # 파이썬에서 빈 문자열 요소 없애기
    # > https://jinmay.github.io/2019/06/30/python/python-how-to-delete-empty-string-in-list/ 참고했음
    target_primes = list(map(int, ' '.join(get_n_digit(n, k).split('0')).split()))  # 0기준으로 쪼개기
    for num in target_primes:  # 쪼갠 숫자 검사
        if num > 1 and is_prime(num):  # 1이하거나 소수 아니면 꺼져
            answer += 1
    return answer


print(solution(110011, 10))
