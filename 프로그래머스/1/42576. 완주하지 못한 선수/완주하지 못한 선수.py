from collections import Counter

def solution(participant, completion):
    return (Counter(participant) - Counter(completion)).most_common().pop()[0]