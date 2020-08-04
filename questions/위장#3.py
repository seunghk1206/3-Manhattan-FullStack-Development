def solution(clothes):
    answer = 0
    n = 1
    count = {}
    for each in clothes:
        try:
            count[each[1]] += 1
        except:
            count[each[1]] = 2
    for val in count.values():
        n *= val
    answer = n-1
    return answer
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))

####
