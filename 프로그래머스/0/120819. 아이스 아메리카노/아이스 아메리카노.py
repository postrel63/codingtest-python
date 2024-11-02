import math
def solution(money):
    answer = []
    americano = 5500
    answer = [math.floor(money / americano) , money % americano]
    
    return answer