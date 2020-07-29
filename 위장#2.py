import itertools
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
    for each in clothes:
        orgL.append(each)
    for each in range(1, len(clothes)):
        tempL.append(list(combinations(orgL, each)))
    print(tempL)
    for each in tempL:
        for _ in each:
            answer += 1
    return answer-1
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])