def solution(citations):
    answer = 0
    tempL = []
    ansL = []
    for each in range(max(citations)+1):
        for eachVar in citations:
            if eachVar >= each:
                tempL.append(eachVar)
        if len(tempL) >= each:
            ansL.append(each)
        tempL = []
    answer += max(ansL)
    return answer