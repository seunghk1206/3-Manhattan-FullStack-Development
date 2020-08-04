def combinations(List, n):
    for index in range(len(List)):
        if n == 1:
            yield [List[index]]
        else:
            for next in combinations(List[index+1:], n-1):
                yield [List[index]] + next
def solution(clothes):
    answer = 0
    tempL = []
    orgL = []
    temp2L = []
    for each in clothes:
        orgL.append(each)
    for each in range(1, len(clothes)):
        tempL.append(list(combinations(orgL, each)))
    answer += len(clothes)
    tempL.remove(tempL[0])
    for each in tempL:
        for eachIt in each:
            for eachVar in eachIt:
                if eachVar[1] == eachIt[eachIt.index(eachVar)-1][1]:
                    pass
                else:
                    temp2L.append(eachIt)
    tempL = []
    orgL = []
    for eachV in temp2L:
        if eachV in tempL:
            pass
        else:
            orgL.append(eachV)
        tempL.append(eachV)
    answer += len(orgL)
    return answer
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))