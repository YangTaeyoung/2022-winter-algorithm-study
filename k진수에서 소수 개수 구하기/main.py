# 프로그래머스 - k진수에서 소수 개수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/92335


import math


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_digit(num: int, digit: int):
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    mok = num
    result = list()
    while True:
        reminder = mok % digit
        mok //= digit
        result.append(num_list[reminder])
        if mok < digit:
            if mok:
                result.append(num_list[mok])
            break
    result.reverse()
    return "".join(result)



def solution(n, k):
    answer = 0
    # 파이썬에서 빈 문자열 요소 없애기
    # > https://jinmay.github.io/2019/06/30/python/python-how-to-delete-empty-string-in-list/ 참고했음
    target_primes = list(map(int, ' '.join(get_n_digit(n, k).split('0')).split()))
    print(target_primes)
    for num in target_primes:
        if num > 1 and is_prime(num):
            answer += 1
    return answer

print(solution(110011,10))