def solution(citations):
    answer = 0
    citations.sort(reverse = True)

    if citations[0] == 0:
        return 0
    
    for i in citations:
        if answer >= i:
            return answer
        answer += 1
        
    return answer