#백준 15686 치킨 배달 G5
#코테 강의에서 나온 문제와 완전히 동일
#좋은 문제, 복습 필요

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = ck[x][0]
                y2 = ck[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(ck)):
            cb[L] = i
            DFS(L + 1, i + 1)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hs = []  #집 좌표 리스트
ck = [] #치킨집 좌표 리스트
cb = [0] * m #살아남을 치킨집의 좌표 리스트
res = 2147000000
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            hs.append((i, j))
        elif board[i][j] == 2:
            ck.append((i, j))
DFS(0, 0) #첫 지점 (0.0)에서 시작
print(res)

