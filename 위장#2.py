import itertools
from itertools import product
from itertools import combinations
def solution(clothes):
    answer = 0
    tempL = []
    orgL = []
    for each in clothes:
        orgL.append([each])
    for each in range(1, len(clothes)):
        tempL.append(list(combinations(orgL, each)))
    print(list(itertools.chain(tempL)))
    for each in tempL:
        for _ in each:
            answer += 1
    return answer-1
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])