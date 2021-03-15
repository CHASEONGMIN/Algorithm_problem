#백준 2606 바이러스 S3
#중요, dfs, bfs 기본문제
#출발 지점이 고정되어 있어서 난이도 낮은편

## 1. 그래프 생성 후 DFS
from sys import stdin
dic = {}

for i in range(int(stdin.readline())):   # 그래프(딕셔너리) 틀 생성
    dic[i+1] = set()   #중복이 없어야 하므로 set 활용해줌

for j in range(int(stdin.readline())):  # 그래프에 값들 넣어줌
    a, b = map(int, stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

def DFS(start, dic): #재귀형식으로 작성
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            DFS(i, dic)
visited = []
DFS(1, dic)
print(len(visited)-1)  #1을 제외한 노드의 개수를 출력해야하므로 -1

## 2. 그래프 생성 후 BFS

from sys import stdin
dic = {}

for i in range(int(stdin.readline())):   # 그래프(딕셔너리) 틀 생성
    dic[i+1] = set()   #중복이 없어야 하므로 set 활용해줌

for j in range(int(stdin.readline())):  # 그래프에 값들 넣어줌
    a, b = map(int, stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

def BFS(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
visited = []
BFS(1, dic)
print(len(visited)-1) #1을 제외한 노드의 개수를 출력해야하므로 -1

