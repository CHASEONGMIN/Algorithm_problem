#백준 1918 후위 표기식 G4
# 스택 관련 기본 문제 중요함.

s = input()
stack = []
res = ''
for x in s:
    if x.isalpha(): #알파벳은 그냥 출력
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':   #stack이 비어 있지 않다는 조건 무조건 들어가야 함!!
            while stack and (stack[-1] == '*' or stack[-1] == '/'): #* /보다 우선순위 낮은것들 pop
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-': #(만나기 전까지 pop
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop() #(도 pop을 해줘야 하므로
while stack: #마지막에 stack에 남은 *도 pop해서 더해줘야 함
    res += stack.pop()
print(res)