#백준 4949 균형잡힌 세상 S4
#스택 기본 문제
#매우 좋은 문제 였음. 굿굿

while True:
    s = input()
    stack = []
    if s == '.':
        break
    for i in range(len(s)):
        if s[i] == '[':
            stack.append(s[i])
        elif s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
        elif s[i] == ']':
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
        elif s[i] == '.':
            break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')