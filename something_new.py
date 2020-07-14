def in_for(num, inp):
    for each in inp:
        if each == num:
            return True
answer = 0
if in_for(5, [5,3,4,2,1,3,4,2,9]) == True:
    answer += 1
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
    return None
if in_bin(5, [5,3,4,2,1,3,4,2,9]) == True:
    answer += 1
print(answer)