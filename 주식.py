def solution(prices):
    length = 0
    someL = []
    answer = []
    for each in range(1, len(prices)):
        for eachAns in range(each, len(prices)-each):
            print(len(prices)-each)
            if prices[each-1] > prices[eachAns]:
                length += 1
                break
            elif prices[each-1] <= prices[eachAns]:
                length += 1
                someL.append(prices[eachAns])
        answer.append(length)
        length = 0
    print(someL)
    answer.append(0)
    return answer
print(solution([1,2,3,2,3]))