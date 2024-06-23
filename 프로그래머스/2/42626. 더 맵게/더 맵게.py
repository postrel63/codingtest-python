import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        pop1 = heapq.heappop(scoville)
        if pop1 >= K:
            return answer
        pop2 = heapq.heappop(scoville)
        sco = pop1 + (pop2 * 2)
        heapq.heappush(scoville, sco)
        answer += 1

    if scoville[0] >= K:
        return answer
    else:
        return -1

    

