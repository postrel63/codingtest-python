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
