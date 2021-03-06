#백준 1934 최소공배수 S5
#A를 B로 나눈 나머지가 R일 때, A와B의 최대공약수는 B와 R의 최대공약수. (B와 A%B의 최대공약수와 동일)
#최소공배수는 두 수의 곱을 두 수의 최소 공배수로 나눈 값과 동일.

def gcd(a , b):  #최대 공약수 구하는 함수 2단계로 나눔
    if a < b:  #1. 주어진 수 중 큰 수가 A여야 하므로 아닐 시 바꿔줌.
        a , b = b , a
    while b!=0: #2. A와 B의 최대공약수가 B와 R의 최대 공약수이므로 이를 이용하여 b가 0이될떄까지 진행
        a , b = b , a % b
    return a

def lcm(a , b): #최소공배수는 두 수의 곱을 두 수의 최소 공배수로 나눈 값과 동일
    return a*b // gcd(a,b)

N = int(input())
for _ in range(N):
    M, K = map(int, input().split())
    print(lcm(M, K))
