#백준 피보나치 함수 실3
#시간 단축을 위해서는 재귀가 아니느 반복문을 사용해주어야 함.
# import sys
# sys.stdin = open('1003.txt', 'r')

def fib(num):
    if num == 0:
        print(1, 0)
    elif num == 1:
        print(0, 1)
    elif num == 2:
        print(1, 1)
    else:  #fib(2)까지는 값이 정해져 있다고 봐도 되므로 조건으로 걸어줌.
        temp = 0
        current = 1 #1출력 용
        before = 0 #0출력 용
        for _ in range(num - 1):
            temp = current
            current = before + temp
            before = temp
        print(before, current)

T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)

# 훨씬 간단한 풀이법 (동적 계획법 활용)
# cnt0 = [1, 0]
# cnt1 = [0, 1]
#
# for i in range(2, 41):
#     cnt0.append(cnt0[i - 1] + cnt0[i - 2])
#     cnt1.append(cnt1[i - 1] + cnt1[i - 2])
#
# for _ in range(int(input())):
#     n = int(input())
#     print(cnt0[n], cnt1[n])

#0을 호출한 횟수와 1을 호출한 횟수를 각각 cnt0, cnt1이라는 리스트로 선언하여 메모이제이션으로 사용한 방법.
