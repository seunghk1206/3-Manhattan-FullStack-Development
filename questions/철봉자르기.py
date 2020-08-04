def solution(arrangement):
    answer = 0
    count = 0
    for each in arrangement:
        if each == '(':
            count += 1 
        elif each == ')':
            count -= 1
            answer += count
    return answer
print(solution('()(((()())(())()))(())'))