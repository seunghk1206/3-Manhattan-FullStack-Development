def solution(clothes):
    answer = 1
    tempL = [x[1] for x in clothes]
    setL = set(tempL)
    for y in setL:
        answer *= tempL.count(y)+1
    return answer-1
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))