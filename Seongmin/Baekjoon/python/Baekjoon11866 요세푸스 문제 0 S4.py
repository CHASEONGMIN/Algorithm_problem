#백준 11866 요세푸스 문제 0 S4
#큐 기본문제

N, K = map(int, input().split())
queue = [i for i in range(1, N+1)]

print('<', end='')
while queue:
    if len(queue) == 1:
        print(queue.pop(), end='')
    else:
        for i in range(K-1):  #사람들 순서 돌림
            queue.append(queue.pop(0))
        print(queue.pop(0), end='')
        print(',', end=' ')
print('>')