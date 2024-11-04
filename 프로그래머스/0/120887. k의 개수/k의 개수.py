def solution(i, j, k):
    answer = 0
    for i in range(i, j +1):
        strNum = str(i)
        answer += strNum.count(str(k))
    
    return answer