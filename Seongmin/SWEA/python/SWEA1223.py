#SWEA 1223 계산기2
# 막힌 부분 검색하여 해결.

# 숫자를 저장하는 스택과 연산자를 저장하는 스택을 운영하여 후위연산으로 만듬.
# (숫자가 나온다면 숫자스택에 넣어주고, 연산자가 나온다면 연산자스택의 이전값의 우선순위를 보고 판단하여 계산)
# 이후에, 남은 연산자를 하나의 스택으로 합쳐주고, 하나의 스택의 데이터를 꺼내며 후위연산을 마무리한다.
# 스택에 남아있는 값이 리턴할 결과값이 된다.

import sys
sys.stdin = open('1223.txt', 'r')

operator = {'*': 1, '+': 2} # 연산자 생성 및 우선순위 넣어줌

def calulate(c1, c2, j):  #계산을 위한 함수
    c1 = int(c1) #타입이 str과 int로 나오므로 형변환 int로 명시적으로 해줘야 함.
    c2 = int(c2)
    if j == '+':
        return c1 + c2
    elif j == '*':
        return c1 * c2

T = 10 #테스트 케이스 10개
for tc in range(1, T + 1):
    l = input() #테스트 케이스의 길이 (이 문제에서는 큰 의미없음 추후에 활용하는게 나올듯?)
    arr = list(input()) # 테스트 케이스를 리스트로 만들어줌.
    stack_operater = [] #연산자 스택 생성
    stack_result = [] #결과용 스택 생성

    for i in arr:
        if '0' <= i <= '9':   # 숫자면 삽입.
            stack_result.append(i)
        elif not len(stack_operater): # 연산자 스택이 비어있다면 연산자 삽입
            stack_operater.append(i)
# 들어온 연산자가 연산자 스택의 안의 가장 위 연산자보다 우선순위가 높다면 추가하기(낮은 수가 높은 우선순위이므로 <)
        elif operator[i] < operator[stack_operater[-1]]:
            stack_operater.append(i)
        else: #이부분이 어려웠음!!!
            # 스택이 비지않거나 들어온 연산자가 스택의 탑보다 크거나 같을때까지
            while len(stack_operater) and operator[i] >= operator[stack_operater[-1]]:
                stack_result.append(stack_operater.pop()) # pop을하고 그 값을 결과 값에 삽입.
            # 반복이 끝난후 연산자스택에 추가하기
            stack_operater.append(i) #위치 주의

    while len(stack_operater): #연산자 스택 정리 단계
        # 연산자 스택이 빌때까지 pop후에 결과스택에 삽입.
        temp = stack_operater.pop()
        stack_result.append(temp)
   # print(stack_result) #제대로 후위 연산 되었나 체크용

#################################후위 연산 끝 ########################

    for j in stack_result: #결과용 스택 순회하며 계산을 해줘야 함.
        if '0' <= j <= '9': # 숫자라면 삽입
            stack_operater.append(j)
        else:
            # 연산자라면 숫자 2개를 꺼내서 계산한다.
            c2 = stack_operater.pop() #여기에서는 순서가 안 중요하지만, 혹시모르니 먼저나오는걸 c2로 함.
            c1 = stack_operater.pop()
            stack_operater.append(calulate(c1, c2, j))

    print('#{} {}'.format(tc, stack_operater[0])) # 결과값 출력