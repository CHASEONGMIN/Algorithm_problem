#백준 10828 스택 실4
# 스택의 기본 구조를 익히기 좋음

import sys
N = int(sys.stdin.readline())

stack = []
for i in range(N):
    order = sys.stdin.readline().split()  #order[0] : 명령어 order[1]: 값

    if order[0] == 'push': # push라면 append
        stack.append(order[1])
    elif order[0] == 'pop': #pop이라면 스택이 비어있는지 체크 후 pop
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':  #size라면 스택의 길이를 출력
        print(len(stack))
    elif order[0] == 'empty': #empty라면 스택이 비어있는지 판별 후 참이면 1, 거짓이면 0 반환        if len(stack) == 0:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top': #top이라면 스택이 비어있는지 체크 후, 아니라면 스택의 가장 뒷부분 출력
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])