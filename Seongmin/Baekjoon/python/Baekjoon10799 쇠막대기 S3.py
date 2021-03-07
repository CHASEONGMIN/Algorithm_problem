#백준 10799 쇠막대기 S3
# 스택 좋은 문제

s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)