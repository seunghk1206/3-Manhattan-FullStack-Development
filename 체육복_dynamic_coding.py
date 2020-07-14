def solution(n, lost, reserve):
    def in_bin(num, inp):
        inp.sort()
        begin_index = 0
        end_index = len(inp)-1
        while begin_index <= end_index:
            midpoint = begin_index + (end_index - begin_index) // 2
            midpoint_value = inp[midpoint]
            if midpoint_value == num:
                return True
            elif num < midpoint_value:
                end_index = midpoint - 1
            elif num > midpoint_value:
                begin_index = midpoint + 1
        return False
    answer = n - int(len(lost))
    for each in lost:
        if in_bin(each, reserve) == True:
            answer += 1
            reserve.remove(each)
        elif in_bin(each-1, reserve) == True and in_bin(each-1, lost) == False:
            answer += 1
            reserve.remove(each-1)
        elif in_bin(each+1, reserve) == True and in_bin(each+1, lost) == False:
            answer += 1
            reserve.remove(each+1)
    return answer
print(solution(3, [1,2], [2,3]))