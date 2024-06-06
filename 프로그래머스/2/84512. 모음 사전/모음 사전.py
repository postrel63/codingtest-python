# 1,2,3,4,5 각각 5개씩, 만들 수 있는 모든 조합(최대 5길이), 정렬, 그리고 word랑 인덱스 비교 
from itertools import permutations, product

def solution(word):
    answer = 0
    list = ['A', 'E', 'I', 'O', 'U']
    setList = []

    for i in range(1, 6):
        for p in product(list, repeat=i):
            setList.append(''.join(p))

    result= sorted(setList)

    return result.index(word)+1
