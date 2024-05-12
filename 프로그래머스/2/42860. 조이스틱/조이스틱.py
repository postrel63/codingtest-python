def solution(name):
    if name.count("A") == len(name):
        return 0

    numList = [min(ord(i) - ord('A'), abs(ord('Z') - ord(i) + 1)) for i in name]
    answer = sum(numList)


    n = len(name)
    move = n - 1 
    for index in range(n):
        nextIndex = index + 1
        while nextIndex < n and name[nextIndex] == 'A':
            nextIndex += 1
        distance = min(index, n - nextIndex)
        move = min(move, index + n - nextIndex + distance)

    return answer + move