#SWEA 4871 그래프 경로 D2
#DFS문제, 스택 활용
#아직 스택이 익숙치 않아서 참고함.

import sys
sys.stdin = open('4871.txt', 'r')

def check(s):
    visited[s] = False  #이미 방문했었다면 False
    for i in gra[s]:
        if visited[i] == True: #간선에 대한 노드가 True면 다시 호출하여 False로 바꿔줘야 함.
            check(i)

T = int(input())

for tc in range(1, T+1):
    v,e = map(int,input().split())
    gra = [[] for _ in range(v+1)] #각 노드의 간선에 대한 노드를 넣기 위해 생성해줌.
    visited  = [True for _ in range(v+1)] #방문여부 체크

    for j in range(e):
        a,b = map(int,input().split())
        gra[a].append(b) #노드의 간선들을 각각 추가해줌.

    s,g = map(int,input().split()) # start노드와 end노드
    check(s)
    result = 1
    if visited[g]==True:
        result = 0
    print('#{} {}'.format(tc, result)) #str로 나타내 주어야 함.