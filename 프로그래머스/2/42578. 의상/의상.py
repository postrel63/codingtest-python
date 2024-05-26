def solution(clothes):
    answer = 1
    array = {}
    for i in clothes:
        if i[-1] in array:
            array[i[-1]] += 1
        else:
            array[i[-1]] = 1

    for i in array:
        answer *= (array[i] + 1)

    return answer - 1