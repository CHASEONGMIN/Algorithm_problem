#백준 9012 괄호 실4
#두가지 풀이법
#주로 풀어야 할 것은 stack


#스택 없이 풀기
T = int(input()) #테스트 케이스의 수

for tc in range(1, T+1):
    arr= list(map(str, input()))
    sum = 0
    for i in arr:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')


#스택 사용하여 풀기

# T = int(input())
# def check(a):
#     stack = []
#     for i in a:
#         if i == '(':
#             stack.append(i)
#         else:
#             if not stack: #)입력 전에 (를 입력받지 않았을 때
#                 print("NO")
#                 return
#             else:
#                 stack.pop() #stack에 (가 있는 상황
#
#     if not stack: #위의 for문을 돌았음에도 stack안에 무언가 있으면 VPS가 아님.
#         print("YES")
#         return
#     else:
#         print("No")
#         return
#
# for _ in range(T):
#     a = input()
#     check(a)


