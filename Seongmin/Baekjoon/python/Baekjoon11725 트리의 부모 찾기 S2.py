#백준 11725 트리의 부모 찾기 S2
# 딕셔너리 활용한 풀이

from collections import deque
import sys
sys.stdin = open('text/11725.txt', 'r')

n = int(input())
tree = [[] for _ in range(n+1)] #트리 리스트 생성

for i in range(n-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)  # 서로 연결해주는 과정
    tree[b].append(a)

q = deque([1]) #시작 노드는 1

visited = [0 for i in range(n+1)]
res = {} # 딕셔너리 활용

while q:
    val = q.popleft()
    for i in tree[val]: # tree[val]의 요소를 꺼냄
        if visited[i] == 0:
            res[i] = val
            visited[i] = 1
            q.append(i)

for i in range(2, n+1):
    print(res[i])



