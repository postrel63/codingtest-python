import heapq


def solution(jobs):
    jobs.sort()

    curtime = 0
    totalTime = 0
    jobCount = len(jobs)
    idx = 0
    pq = []

    while idx < jobCount or pq:
        while idx < jobCount and jobs[idx][0] <= curtime:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if pq:
            duration, start_time = heapq.heappop(pq)
            curtime += duration
            totalTime += curtime - start_time
        else:
            if idx < jobCount:
                curtime = jobs[idx][0]
    answer = totalTime // jobCount
    return answer
