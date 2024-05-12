def solution(people, limit):
    answer = 0
    people.sort()
    rt, lt = 0, len(people) - 1

    while rt <= lt:
        if people[lt] + people[rt] <= limit:
            rt += 1
        lt -= 1
        answer += 1

    return answer
