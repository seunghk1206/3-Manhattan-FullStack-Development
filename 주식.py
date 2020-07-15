def solution(prices):
    length = 0
    someL = []
    answer = []
    for i in range(0, len(prices) - 1):
        for j in range(i+1, len(prices) - 1 - i):
            if prices[i] > prices[j]:
                length += 1
                break
            elif prices[i] <= prices[j]:
                length += 1
                someL.append(prices[j])
        answer.append(length)
        length = 0
    print(someL)
    answer.append(0)
    return answer
print(solution([1,2,3,2,3]))
