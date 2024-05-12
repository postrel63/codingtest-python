from collections import deque

def solution(number, k):
    dq = deque()
    for i in number:
        while k > 0 and dq and dq[-1] < i:
            dq.pop()
            k -= 1
        dq.append(i)

    for _ in range(k):
        dq.pop()

    return ''.join(map(str,dq))
