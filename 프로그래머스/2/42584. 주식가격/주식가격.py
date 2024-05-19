def solution(prices):
    plen = len(prices)
    answer = [0] * plen

    for i in range(plen):
        for j in range(i + 1, plen):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer