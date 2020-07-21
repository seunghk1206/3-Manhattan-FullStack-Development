def solution(priorities, location):
    answer = 0
    run = 1
    while run == 1:
        if priorities[0] != max(priorities):
            print(location)
            priorities.append(priorities.pop(0))
            if location == 0:
                location += len(priorities)
            else:
                location -= 1
        else:
            priorities.remove(max(priorities))
            answer += location
    return answer
print(solution([9, 1, 2, 3, 1, 1, 1, 1], 3))