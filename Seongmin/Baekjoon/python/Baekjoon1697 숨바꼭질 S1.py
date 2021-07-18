#백준 1697 숨바꼭질 S1
#BFS

from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        #각 queue안의 지점에 대해 v-1, v+1, v*2를 해줘야 함.
        for next_turn in (v - 1, v + 1, v * 2):
            if 0 <= next_turn < 100001 and not time[next_turn]:
                time[next_turn] = time[v] + 1
                q.append(next_turn)

N, K = map(int, input().split())
time = [0] * 100001
bfs()
