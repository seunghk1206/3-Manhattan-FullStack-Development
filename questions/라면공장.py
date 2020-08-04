def solution(stock, dates, supplies, k):
    answer = 0
    run = 1
    tempL = []
    compL = []
    while run == 1:
        for each in dates:
            if each <= stock:
                tempL.append(dates.index(each))
        for each in tempL:
            compL.append(supplies[each])
        tempL.reverse()
        for each in tempL:
            supplies.pop(each)
            dates.pop(each)
        stock += max(compL)
        answer += 1
        compL = []
        tempL = []
        if stock >= k:
            run = 0
    return answer