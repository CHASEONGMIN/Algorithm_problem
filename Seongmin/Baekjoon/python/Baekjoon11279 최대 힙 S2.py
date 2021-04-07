#백준 11279 최대 힙 S2
#최소힙과 동일하지만, push할 때 -붙이고 넣어주고 pop할때도 -를 붙여주면 최대값부터 출력이 됨을 활용
#시간초과가 발생하여 input()를 사용하지 않고 sys.stdin.readline()사용

import sys
import heapq as hq

heap = []

n = int(sys.stdin.readline())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-hq.heappop(heap))
    else:
        hq.heappush(heap, -i)


