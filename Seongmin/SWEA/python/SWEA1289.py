#SWEA 1289 원재의 메모리 복구하기 D3
#인덱스 다루는 문제

import sys
sys.stdin = open('1289.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    before = list(input()) #초기 메모리 값
    mem = ['0']*len(before) #바꿔줘야 할 메모리 값
    cnt = 0 #수정횟수
    #초기 메모리 값과 바꿔줘야 할 메모리값들이 같은지 비교하고 다를때마다 mem의 이후 길이만큼을 모두 바꿔주고 cnt 카운트를 증가시킨다.
    for i in range(len(mem)):
        if mem[i] != before[i]:
            mem[i:] = before[i]*len(mem[i:])
            cnt += 1

    print('#{} {}'.format(tc, cnt))
