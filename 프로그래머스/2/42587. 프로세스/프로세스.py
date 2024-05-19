from collections import deque
def solution(priorities, location):
    answer = 0
    dq = deque([(value, idx) for idx, value in enumerate(priorities)])
    priorities.sort()
    
    while dq:
        
        cur = dq.popleft()
        if not all(cur[0] >= i[0] for i in dq):
            dq.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                break
    
    return answer