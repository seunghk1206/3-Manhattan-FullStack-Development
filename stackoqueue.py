def solution(priorities, location):
    answer = 0
    run = 1
    nb = []
    while run == 1:
        if len(priorities) == 0:
            answer += location
            run = 0
        elif priorities[0] != max(priorities):
            priorities.append(priorities.pop(0))
            if location == 0:
                location += len(priorities)
            else:
                location -= 1
        else:
            nb.append(max(priorities))
            priorities.remove(max(priorities))
    return answer
print(solution([9, 1, 2, 3, 1, 1, 1, 1], 3))