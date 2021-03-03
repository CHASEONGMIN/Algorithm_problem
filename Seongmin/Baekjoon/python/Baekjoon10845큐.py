#백준 10845 큐 실4
# 큐의 기본 구조를 익히기 좋음
#10828 스택과 비교하며 보면 더 이해가 잘될것.

import sys
N = int(sys.stdin.readline())

queue = []
for i in range(N):
    order = sys.stdin.readline().split()  #order[0] : 명령어 order[1]: 값

    if order[0] == 'push': # push라면 append
        queue.append(order[1])
    elif order[0] == 'pop': #pop이라면 큐가 비어있는지 체크 후 pop
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
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