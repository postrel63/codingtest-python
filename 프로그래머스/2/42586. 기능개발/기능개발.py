 # while 문으로 시간 day 똑같이 반복
# for 문으로 progresses 반복하면서 progresses + speeds x day >= 100 이면 정지
# progresses의 앞순서의 진도율이 100이 넘는 걸 매번 체크해서 넘는 순간에 그 작업과 연속된 뒤의 작업들까지 모두 answer에 담아줌
# 다시 반복


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