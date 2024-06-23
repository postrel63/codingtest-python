def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1

    for i, j in puddles:
        graph[j - 1][i - 1] = -1

    for i in range(m):
        if graph[0][i] == -1:
            break
        graph[0][i] = 1

    for i in range(n):
        if graph[i][0] == -1:
            break
        graph[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            # 물 웅덩이면 0으로
            if graph[i][j] == -1:
                graph[i][j] = 0
            else:
                #  물 웅덩이 아니면 값 더하기
                if graph[i - 1][j] != -1:
                    graph[i][j] += graph[i - 1][j]
                if graph[i][j - 1] != -1:
                    graph[i][j] += graph[i][j - 1]
                graph[n - 1][m - 1] %= 1000000007

    return graph[n - 1][m - 1]