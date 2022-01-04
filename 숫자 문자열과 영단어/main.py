num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}


# 직접 풀었던 해답
def solution_1(s):
    answer = []
    num_stack = []
    for char in s:
        if char.isnumeric():
            answer.append(str(int(char)))
        else:
            num_stack.append(char)
            if len(num_stack) >= 3:
                try:
                    answer.append(num_dict[''.join(num_stack)])
                    num_stack = []
                except KeyError:
                    pass
    answer = int(''.join(answer))
    return answer


# 다 풀고 나니 다른 사람이 푼 접근 중 더 좋은 해답이 있었음.
# 파이썬 replace 함수를 이용한 해답
def solution_2(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(words)):
        s = s.replace(words[i], str(i))
    return int(s)
