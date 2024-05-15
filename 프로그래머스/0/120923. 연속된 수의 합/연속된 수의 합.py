def solution(num, total):
    first = int(total // num - num // 2 ) 
    if num & 1 == 0:
        first += 1  
    answer = [i for i in range(first,first + num,1)]
    return answer