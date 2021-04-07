#백준 1927 최소 힙 S1
#11279 최대 힙과 11286 절댓값 힙과 비슷한 문항
#최대힙과 동일하지만, push할 때 그냥 넣어주고 pop할때도 그냥 출력하면 최소값부터 출력이 됨을 활용
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
            print(hq.heappop(heap))
    else:
        hq.heappush(heap, i)