def solution(s):
    def insertion_sort(A):
        for each in range(0, len(A)):
            for i in range(0, len(A)):
                if len(A[each]) < len(A[i]):
                    A[each], A[i] = A[i], A[each]
        return A
    answer = []
    tempL = [each for each in s if each not in ['{', '}']]
    answer2 = []
    tempStr = ''
    for each in tempL:
        if each == ',':
            answer.append(tempStr)
            tempStr = ''
        else:
            tempStr += each
    answer.append(tempStr)
    answer = insertion_sort(answer)
    for each in answer:
        if int(each) in answer2:
            pass
        else:
            answer2.append(int(each))
    return answer2