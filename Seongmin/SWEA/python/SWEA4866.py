#SWEA 4866 괄호검사 D2
#복습 필요 스택 문제

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    value = input()
    stack = [] # 스택 생성

    for i in range(len(value)): #입력된 길이 만큼

        if value[i] == "(" or value[i] == "{":
            stack.append(value[i])  #여는 괄호는 바로 추가해줌
        elif value[i] == ")" or value[i] == "}":

            #닫는 괄호 이면 스택을 체크해 줘야 함.
            if len(stack) == 0: #stack이 비어있다면 처음부터 닫는 괄호가 오는 경우이므로 스택에 넣어줌
                stack = [value[i]]
                break
            #stack에 저장된 괄호와 일치하지 않는 경우
            elif (value[i] == "}" and stack[-1] !="{") or (value[i] == ")" and stack[-1] != "("):
                stack = [value[i]] #스택에 마찬가지로 넣어줌
                break
            #stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
            else:
                stack.pop()

    if not len(stack): #스택이 비어있다면
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')