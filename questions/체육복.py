def solution(n, lost, reserve):
    answer = n - int(len(lost))
    for each in lost:
        if each in reserve:
            answer += 1
            reserve.remove(each)
        elif each-1 in reserve and each-1 not in lost:
            answer += 1
            reserve.remove(each-1)
        elif each+1 in reserve and each+1 not in lost:
            answer += 1
            reserve.remove(each+1)
    return answer
print(solution(3, [1,2], [2,3]))