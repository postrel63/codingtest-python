# 2 < 0 
# 0 < 5
# 5 < 2
def solution(rsp):
    answer = ''
    list = [2, 0, 5]
    for i in rsp:
        if (i == '2'):
            answer += '0'
        elif (i == '0'):
            answer += '5'
        else:
            answer += '2'
    
    return answer