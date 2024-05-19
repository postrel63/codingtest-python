
# or 각 항목마다 며칠뒤에 끝나는지 리스트로 다 만들고 한번에 계산
import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    list = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(speeds))]
        
    dq = deque(list)
    while dq:
        cur = dq.popleft()
        cnt = 1
        while dq and dq[0] <= cur:
            dq.popleft()
            cnt += 1
        answer.append(cnt)

    return answer