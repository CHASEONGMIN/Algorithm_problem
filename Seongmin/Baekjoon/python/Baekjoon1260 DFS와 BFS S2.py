#백준 1260 DFS와 BFS S2
# 매우 중요한 기본 문제
#인접 행렬 작성

from sys import stdin
n, m, v = map(int, stdin.readline().split())
arr = [[0] * (n + 1) for _ in range(n + 1)] #숫자가 1부터이므로 0은 사용하지 않을 것.
for _ in range(m):
    pos = list(map(int, stdin.readline().split())) #간선 표시
    arr[pos[0]][pos[1]] = 1
    arr[pos[1]][pos[0]] = 1 #양쪽 모두 체크해주어야 하므로 01, 10 모두 체크

# dfs, bfs 진행
def dfs(start, visited): #시작점은 주어지는 v, 다녀왔는지 체크를 위한 visited 활용
    visited += [start]
    for c in range(len(arr[start])): #start의 간선의 개수만큼 반복해서 진행
        if arr[start][c] == 1 and (c not in visited): #간선이고, 방문하지 않았었다면
            dfs(c, visited)  #그 간선으로 이동하여 반복적으로 진행
    return visited 

def bfs(start):
    visited = [start]
    queue = [start] #큐 생성
    while queue:
        n = queue.pop(0) #for문 끝날 때 마다 pop하고 다음번 진행
        for c in range(len(arr[start])): #start의 간선의 개수만큼 반복해서 진행
            if arr[n][c] == 1 and (c not in visited): #간선이고, 방문하지 않았었다면
                visited.append(c) #방문목록에 추가하고
                queue.append(c) #큐에 추가
    return visited

print(*dfs(v,[]))
print(*bfs(v))

