#SWEA 4873 반복문자 지우기 D2
# 스택활용, Top 포인터 활용 top과 top-1의 값 비교하여 pop 해주면 끝

import sys
sys.stdin = open('4873.txt', 'r')

def check(str):
    top = 0
    for i in range(len(str)):
        if len(stack) == 0: #스택 안에 아무것도 없는 경우 추가해줌.
            stack.append(str[i])
        else:
            stack.append(str[i]) #이미 스택안에 다른게 있으면 top포인터 1 증가시켜주고 추가
            top += 1

            if stack[top] == stack[top-1]: #가장 끝쪽 두 값이 같으면 둘다 pop시키고 top포인터 옮김
                stack.pop(top)
                stack.pop(top-1)
                top = top-2

T = int(input())

for tc in range(1, T+1):
    str=input() # 문자열 입력받음
    stack=[]
    check(str)
    print('#{} {}'.format(tc, len(stack)))


