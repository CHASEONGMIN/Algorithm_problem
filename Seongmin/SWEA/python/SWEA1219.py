#SWEA1219 길찾기 D4
#DFS 활용  (못품)
# 문제 오류 수정 7번은 9번으로 연결되고, 아래 그림 4번은 3번으로 수정
# 아직은 쉽지 않아서 참고함.
#인접리스트를 딕셔너리 형태로 만들었다는 점이 새로웠음.

import sys
sys.stdin = open('1219.txt', 'r')

for _ in range(1, 11): # input안에 10개의 테스트 케이스가 있으므로
    tc, n = map(int, input().split())

    # 인접 리스트를 딕셔너리 형태로 생성. (각각이 어디로 갈 수 있는지 나타냄)

    adj_list = list(map(int, input().split()))
    adj = {x: [] for x in range(100)}
    for i in range(0, n * 2, 2): #순서쌍으로 값이 주어지므로[i]와 [i+1]로 나누어 딕셔너리에 넣음
        s = adj_list[i]
        e = adj_list[i + 1]
        adj[s].append(e)

    stack = [0] # 스택 생성

    # 중복탐색을 막기 위해 visited를 활용
    visited = [0] * (100) #0부터 99까지니까 100
    visited[0] = 1 #초기값은 1로 넣어줘야 됨

    res = 0
    while stack:
        i = stack.pop() # 중요
        for side in adj[i]:
            if side == 99:  # 끝점을 만나면 B에 도착한거니 1을 담아주고 break
                res = 1
                break
            if visited[side] == 0: #가보지 않은곳이라면 스택에 추가
                stack.append(side)
                visited[side] = 1

    print('#{} {}'.format(tc, res))


