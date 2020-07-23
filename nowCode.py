def solution(land):
    answer = 0
    reselect = []
    tempL = {}
    tempLB = []
    for eachNum in range(len(land)):
        tempL[eachNum] = land[eachNum]
    for e in land:
        tempLB.append(e)
    for i in range(4):
        x = 0
        del tempLB[:]
        for key, var in tempL.items():
            tempLB.append(var)
        for _ in range(i):
            tempLB[0].remove(max(tempLB[0]))
        print(tempL)
        for each in tempLB:
            try:
                tempLB[tempLB.index(each)+1].pop(each.index(max(each)))
                x += max(each)
            except:
                pass
        reselect.append(x)
    print(reselect)
    answer += max(reselect)
    return answer
solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])