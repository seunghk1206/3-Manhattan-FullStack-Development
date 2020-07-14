def solution(prices):
    length = 0
    answer = []
    for each in range(1, len(prices)):
        for eachAns in range(each, len(prices)-each+1):
            if prices[each-1] <= prices[eachAns]:
                length += 1
            elif prices[each-1] > prices[eachAns]:
                length += 1
                print(length)
                break
        print(length)
        answer.append(length)
        length = 0
    answer.append(0)
    return answer
print(solution([1,2,3,2,3]))