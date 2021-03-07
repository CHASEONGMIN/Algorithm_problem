#백준 1935 후위 표기식2 S3
#1918 후위 표기식에 이어서 보면 됨
# 스택 관련 기본 문제.
def cal(c1, c2, operator): #연산을 해주는 함수 생성
    if operator == '+':
        return c1 + c2
    if operator == '-':
        return c1 - c2
    if operator == '*':
        return c1 * c2
    if operator == '/':
        return c1 / c2


num = int(input())
s = input()
arr_num = [0] * num #알파벳들에 대응하는 값을 받기 위한 리스트 생성

for i in range(num):
    arr_num[i] = int(input())

stack = []

for i in s:
    if 'A' <= i <= 'Z': # 알파벳을 만나면
        stack.append(arr_num[ord(i) - ord('A')])#arr_num 리스트의 인덱스에 맞춰 변환 후, 스택에 저장한다.
    else:  #연산자일 때
        c2 = stack.pop() #먼저 나온것이 2
        c1 = stack.pop()
        stack.append(cal(c1, c2, i))

print('%.2f' %stack[0])  #스택에 남아있는 값 소수점 둘째자리까지 출력함.
