# 문제 해석하는게 가장 어려웠음

n = int(input())
stack = [] # 스택 생성
res = []

flag = 0 # flag가 0이면 res 안의 요소들 출력, 아니면 그냥 끝
criteria = 1
for i in range(n):
    num = int(input())
    while criteria <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(criteria)
        res.append("+")
        criteria += 1

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        res.append("-")
    else:           # **핵심. stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO") # 오름차순으로 스택이 입력되는데 TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있으므로 안됨
        flag = 1
        break

if flag == 0:
    for i in res:
        print(i)