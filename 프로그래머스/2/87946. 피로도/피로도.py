# 백트래킹 
def dfs(k, cnt, dungeons, visited):
    maxCount = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            maxCount = max(maxCount, dfs(k - dungeons[i][1], cnt + 1, dungeons, visited))
            visited[i] = False
    
    return maxCount
        
def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, 0, dungeons, visited)