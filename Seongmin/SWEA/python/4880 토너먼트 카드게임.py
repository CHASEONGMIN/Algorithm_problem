#SWEA4880 토너먼트 카드게임 D2
#코드 참고함.
import sys
sys.stdin = open('4880.txt', 'r')


def judge(a, b):
    # 1: 가위, 2:바위,3:보
    answer = (a - b) % 3
    if answer == 1 or answer == 0: # 0 비김 1 승리 2 패배(a 기준)
        return True
    return False

def game(group):
    if len(group) < 2:
        return group[0]
    group_1, group_2 = [], [] # 그룹을 계속 나눠주고 계산
    j = len(group)
    for i in range(j):
        if i <= (j - 1) // 2:  # 작은번호를 a 에 넣고 계산
            group_1.append(group[i])
        else:
            group_2.append(group[i])
    a = game(group_1)
    b = game(group_2)
    if judge(a[0], b[0]):
        return a
    else:
        return b

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = [(i, idx) for idx, i in enumerate(arr)] #인덱스와 값을 함께 활용해주기 위해 enumerate 활용
    res = game(arr)
    print('#{} {}'.format(tc, res[1] + 1))