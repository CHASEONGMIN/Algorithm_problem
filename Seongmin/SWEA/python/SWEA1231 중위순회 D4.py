#SWEA1231 중위순회 D4
#형변환에 신경을 써줘야 함.

import sys
sys.stdin = open('1231.txt', 'r')

def inorder(n): #중위 순회를 돌려줌.
    if tree[n] != 0: #n이 0보다 크면
        inorder(n * 2)
        print(tree[n], end='')
        inorder(n * 2 + 1)

for tc in range(1, 11): # 10개의 테스트 케이스 주어지고 #1부터 출력
    N = int(input())
    tree = [0] * (101) # 정점의 총 수는 100이 최대이므로 여유있게 101까지 설정

    for i in range(1, N+1):
        value = list(map(str, input().split())) #문자열이껴있으므로 str로 받아준다

        index = int(value[0]) #str로 받아왔으므로 int로 형변환해줘야 함.
        tree[index] = value[1]

    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()

