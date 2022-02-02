# 프로그래머스 - n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


# num을 digit 진수로 변환
def get_n_digit(num: int, digit: int):
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


def solution(n, t, m, p):
    answer = list()
    digits = ""  # 구할 진수 숫자가 들어갈 곳임
    i = 0
    # 진수 변환 후 숫자 붙이는 과정 1,2,3,4 => 0011011100
    while len(digits) < t * m + p - 1:
        digits += get_n_digit(i, n)
        i += 1
    # 자기 순서에 해당하는 수만 answer 리스트에 넣는 과정
    for i in range(t):
        answer.append(digits[i * m + p - 1])

    return "".join(answer)


print(solution(16, 16, 2, 2))
