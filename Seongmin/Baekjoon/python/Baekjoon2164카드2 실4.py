#백준 2164 카드2 실4
#시간초과.. 고려 -> deque활용
import sys 
from collections import deque 
N = int(sys.stdin.readline()) 
queue = deque() 

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1: 
    queue.popleft() 
    queue.append(queue.popleft()) 

print(queue.pop())





#시간고려 안한 내 해답
# N = int(sys.stdin.readline())
# queue = [i for i in range(1, N + 1)]
# 
# while len(queue) > 1:
#     queue.pop(0)
#     queue.append(queue.pop(0))
#     continue
# 
# print(*queue)

