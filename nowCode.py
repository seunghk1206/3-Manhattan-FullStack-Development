def solution(land):
    answer = 0
    reselect = []
    tempL = []
    for eachList in land:
        tempL.append(eachList)
    for i in range(4):
        x = 0
        land = []
        #for _ in range(i):
        #    land[0].remove(max(land[0]))
        print(tempL)
        for each in land:
            try:
                land[land.index(each)+1].pop(each.index(max(each)))
                x += max(each)
            except:
                pass
        reselect.append(x)
    print(reselect)
    answer += max(reselect)
    return answer
solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])