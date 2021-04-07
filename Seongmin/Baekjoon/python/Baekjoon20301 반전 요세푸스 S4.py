#백준 20301 반전 요세푸스 S4
#백준 11866 요세푸스 문제 0 S4를 바탕으로
#deque 활용, 시간 초과 유의

from collections import deque
N, K, M = map(int, input().split())
queue = deque(i for i in range(1, N+1))
cnt = 0
while queue:
    if cnt//M % 2 == 0:
        for _ in range(K-1): #원래 순서라면 인덱스가 0부터이므로 K-1번 돈다
            queue.append(queue.popleft())
    else:
        for _ in range(K): #사람들 순서 반대로(우측으로) 돌때는 K번 돈다.
            queue.appendleft(queue.pop())
    cnt += 1
    print(queue.popleft())

    # if cnt == M:
    #     for i in range(K - 1):  #
    #         queue.insert(0, queue.pop())
    #     print(queue.pop(0))
    #     cnt += 1
    # else:
    #     for i in range(K-1):  #사람들 순서 돌림
    #         queue.append(queue.pop(0))
    #     print(queue.pop(0))
    #     cnt += 1
