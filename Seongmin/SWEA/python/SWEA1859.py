#SWEA1859 백만 장자 프로젝트 D2
#key : 어떻게 큰수가 나온 이후에 다시  분기를 넣어줄 것인가?
#solution : 탐색을 앞에서하는게 아니라 뒤에서 부터 하면 여러번 탐색하는게 아니라 한번만에 끝낼 수 있음.
#뒤에서 부터 탐색하며 값이 낮아졌다가 기준값보다 올라가게되면 그 전까지의 차를 더하면서 구함.

import sys
sys.stdin = open('1859.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))

    #배열을 뒤집고 이후에 탐색 시작
    arr = arr[::-1]
    m_value = arr[0] #첫 원소를 최대값으로 저장
    sum = 0
    for i in range(1,len(arr)):
        if m_value > arr[i]: # 최대값보다 작으면 sum에 더해줌
            sum += m_value - arr[i]
        else: #최대값보다 크거나 같으면 새로운 최대값으로 저장
            m_value = arr[i]
    print("#{} {}".format(tc, sum))
