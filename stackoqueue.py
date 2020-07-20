def solution(priorities, location):
    answer = 0
    run = 1
    while run == 1:
        if priorities[0] < max(priorities):
            print(location)
            priorities.append(priorities.pop(0))
            if location == 0:
                location += len(priorities)
                location -= 1
            else:
                location -= 1
        else:
            answer += location
            answer += 1
            return answer
            break
print(solution([2, 2, 2, 2, 2], 2))