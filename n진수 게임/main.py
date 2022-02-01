num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


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
    digits = ""
    i = 0
    while len(digits) < t * m + p - 1:
        digits += get_n_digit(i, n)
        i += 1
    print(digits)
    for i in range(t):
        answer.append(digits[i * m + p - 1])

    return "".join(answer)

print(solution(16,16,2,2))