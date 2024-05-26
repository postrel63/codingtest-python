def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        ans = []
        for j in range(commands[i][0]-1, commands[i][1], 1):
            ans.append(array[j])
        ans.sort()
        answer.append(ans[commands[i][2]-1])

    return answer