#백준 10866 덱 S4
# 18258 큐2와 매우 비슷

from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    order = sys.stdin.readline().split()  #order[0] : 명령어 order[1]: 값
    if order[0] == 'push_front': # push front이라면 appendleft
        queue.appendleft(order[1])
    elif order[0] == 'push_back': # push_bakc이라면 append
        queue.append(order[1])
    elif order[0] == 'pop_front': #pop front라면 큐가 비어있는지 체크 후 popleft
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == 'pop_back': #pop back이라면 큐가 비어있는지 체크 후 pop
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif order[0] == 'size':  #size라면 큐의 길이를 출력
        print(len(queue))
    elif order[0] == 'empty': #empty라면 큐가 비어있는지 판별 후 참이면 1, 거짓이면 0 반환
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front': #front라면 큐가 비어있는지 체크 후, 아니라면 큐의 가장 앞부분 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == 'back': #back이라면 큐가 비어있는지 체크 후, 아니라면 큐의 가장 뒷부분 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
