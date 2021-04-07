#백준 11286 절댓값 힙 S1
# 11279 최대 힙과 1927 최소 힙과 비슷한 문항
# 시간초과가 발생하여 input()를 사용하지 않고 sys.stdin.readline()사용
# 절대값이 작다는건 최소힙을 베이스로 절대값 비교하는 부분만 넣어주면 됨.
# Key : 튜플 활용(단, 변수 하나를 따로 선언하여 튜플형태로 저장해둔 이후 변수를 이용해서 기입해야 argument()에러 안뜸)

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
            print(hq.heappop(heap)[1])
    else: # 일단 heap에는 그냥 넣음
        value = (abs(i), i)
        hq.heappush(heap, value)