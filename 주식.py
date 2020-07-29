def solution(prices):
    length = 0
    answer = []
    for i in range(0, len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                length += 1
                break
            elif prices[i] <= prices[j]:
                length += 1
        answer.append(length)
        length = 0
    answer.append(0)
    return answer
print(solution([1,2,3,2,3]))