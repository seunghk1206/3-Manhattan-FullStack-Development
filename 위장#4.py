def solution(clothes):
    answer = 1
    for y in set([x[1] for x in clothes]): answer *= [x[1] for x in clothes].count(y)+1
    return answer-1
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))