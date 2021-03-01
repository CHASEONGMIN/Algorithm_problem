#백준 10942 팰린드롬? 골2
# DP 구간 만드는연습 필요
# 복습 필수
import sys

N = int(input())
DP = [[0 for _ in range(N)] for _ in range(N)] #DP NXN 이중리스트로 생성
# num = list(map(int, input().split())) #N개의 숫자 들어옴
num = [int(i) for i in sys.stdin.readline().split()]

# 순서를 만드는게 중요 함
# (1,2), (2,3), (3,4), (4,5)
# (1,3), (2,4), (3,5)
# (1,4), (2,5)
# (1,5)
# N =5일 때 위와같은 순서처럼 나오게 만들어야 함.

#### 아래 풀이는 2중 for문이라 시간초과 발생 #####

# for k in range(N): # 0~ N-1
#     for start in range(N): # 시작점과 끝점으로 나타내어 보기 편하게 설정
#         end = start + k
#         if end >= N: # 범위 초과시 break
#             break
#         if start == end: # 길이가 1이면 무조건 1
#             DP[start][end] = 1
#             continue
#         if start + 1 == end:
#             if num[start] == num[end]: #길이가 2일 때
#                 DP[start][end] = 1
#                 continue
#         if num[start] == num[end] and DP[start + 1][end - 1]: #길이가 3이상일 때
#             DP[start][end] = 1

for i in range(N): #길이가 1일 때
    DP[i][i] = 1

for i in range(N-1): #길이가 2일 때
    if num[i] == num[i+1]:
        DP[i][i+1] = 1

for i in range(2, N): #길이가 3이상일 때
    for j in range(N-i):
        if num[j] == num[j+i] and DP[j+1][j+i-1] == 1:
            DP[j][j+i] = 1

Q = int(input())   #질문 받음
for i in range(Q):
    # S, E = map(int, input().split())
    S, E = [int(p) for p in sys.stdin.readline().split()]
    print(DP[S - 1][E - 1])