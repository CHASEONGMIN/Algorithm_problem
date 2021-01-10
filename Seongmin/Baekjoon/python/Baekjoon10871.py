N, X = map(int, input().split()) #(1 ≤ N, X ≤ 10,000)
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
#print(b, end = " ") 줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제