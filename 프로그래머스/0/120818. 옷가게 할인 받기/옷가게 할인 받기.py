import math

def solution(price):
    answer = 0
    if (10 > price and price > 1000000):
        return 0
    
    if price >= 500000:
        return math.floor(price * 0.80)
    elif price >= 300000:
        return math.floor(price * 0.90)
    elif price >= 100000:
        return math.floor(price * 0.95)
    else:
        return price
    
    return answer 
        