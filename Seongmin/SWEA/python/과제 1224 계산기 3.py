#SWEA1224 계산기3 D4

operator = {'(': 4, ')': 4, '*': 2, '+': 3,}

def cal(t1, t, t2):
    t1 = int(t1)
    t2 = int(t2)
    if t == '+':
        return t1 + t2
    elif t == '*':
        return t1 * t2

T = 10
for a in range(1, T + 1):
    input()
    t_input = list(input())
    stack_operater = []
    stack_result = []

    for t in t_input:
        # 숫자면 넣는다.
        if '0' <= t <= '9':
            stack_result.append(t)
        # 여는 괄호거나 스택이 비어있거나 스탭탑이 여는 괄호라면 연산자 집어넣기
        elif t == '(' or not len(stack_operater) or stack_operater[-1] == '(':
            stack_operater.append(t)
        # 들어온 연산자가 스택의 연산자보다 우선순위가 높다면 추가하기(낮은 수가 높은 우선순위)
        elif operator[t] < operator[stack_operater[-1]] and t != ')':
            stack_operater.append(t)
        else:
            # 위의 내용에 해당하지 않는다면
            # 스택이 비지않거나 들어온 연산자가 스택의 탑보다 크거나 같을때까지 반복한다.
            while len(stack_operater) and operator[t] >= operator[stack_operater[-1]]:
                # 닫는 괄호라면 괄호없애고 정지한다.
                if stack_operater[-1] == '(':
                    stack_operater.pop()
                    break
                # 위의 조건에 해당하지 않는다면 결과 스택에 추가한다.
                stack_result.append(stack_operater.pop())
            # 반복이 끝난후 닫는괄호가 아닐때만 연산자스택에 추가하기
            if t != ')':
                stack_operater.append(t)

    # 남은 연산자를 처리한다.
    while len(stack_operater):
        # 스택이 빌때까지 결과스택에 넣어준다.
        temp = stack_operater.pop()
        if temp != '(':
            stack_result.append(temp)

    # 후위연산 스택을 순회하면서 확인
    for t in stack_result:
        # 숫자라면 임시저장
        if '0' <= t <= '9':
            stack_operater.append(t)
        else:
            # 연산자면 2개를 꺼내서 계산한다.
            t2 = stack_operater.pop()
            t1 = stack_operater.pop()
            stack_operater.append(cal(t1, t, t2))
    else:
        # 결과값 출력
        print('#{} {}'.format(a, stack_operater[0]))