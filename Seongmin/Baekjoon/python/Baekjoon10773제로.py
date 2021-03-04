#백준10773 제로 실4
import sys

K = int(sys.stdin.readline())
stack = []
for _ in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))


