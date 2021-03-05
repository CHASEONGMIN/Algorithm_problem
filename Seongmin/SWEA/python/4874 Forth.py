#SWEA 4874 Forth D2
import sys
sys.stdin = open('4874.txt', 'r')

def calulate(c1, c2, j): #연산을 진행하기 위해 만든 함수
    c1 = int(c1)
    c2 = int(c2)
    if j == '+':
        return c1 + c2
    elif j == '-':
        return c1 - c2
    elif j == '*':
        return c1 * c2
    elif j == '/':
        return c1 // c2

T = int(input())

for tc in range(1, T + 1):
    stack_result = input().split()
    stack_result.pop()
    stack_operater = []

    # 후위연산 스택을 순회하면서 확인
    for i in stack_result:
        if i.isdigit():  # 숫자라면 임시저장
            stack_operater.append(i)
        else:
            if len(stack_operater) < 2:
                print('#{} error'.format(tc)) 
                break
            # 연산자면 2개를 꺼내서 계산한다.
            c2 = stack_operater.pop()  #먼저 나오는게 2번째 이므로 c2로 함
            c1 = stack_operater.pop()
            stack_operater.append(calulate(c1, c2, i))
    else: # 결과값 출력
        if len(stack_operater) != 1:
            print('#{} error'.format(tc))
            continue
        print('#{} {}'.format(tc, stack_operater[0]))