#백준 1018 체스판 다시 칠하기 실 5 중요
# 난이도 있음
# 해설 참조함 복습 필수 
# 접근법 중요 how? 구간을 만들고(8 * 8) 구간탐색을 진행
# 브루트포스 문제, 흰색이 먼저인지 검은색이 먼저인지 분기처리
# import sys
# sys.stdin = open('1018.txt', 'r')

n, m = map(int, input().split())
arr = [] #체스판을 받아오기 위한 리스트
res = [] #결과 저장을 위한 빈 리스트

for _ in range(n):
    arr.append(input())

for i in range(n - 7):
    for j in range(m - 7):    #구간을 만들어줌
        idx1 = 0
        idx2 = 0
        for r in range(i, i + 8):
            for c in range(j, j + 8):     # 구간을 B와 W로 번갈아가면서 탐색
                if (c + r) % 2 == 0:
                    if arr[r][c] != 'W': idx1 += 1
                    if arr[r][c] != 'B': idx2 += 1
                else :
                    if arr[r][c] != 'B': idx1 += 1
                    if arr[r][c] != 'W': idx2 += 1
        res.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        res.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(res))                                   # 칠해야 하는 개수의 최소값