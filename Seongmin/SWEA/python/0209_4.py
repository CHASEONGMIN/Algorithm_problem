#SWEA 4835 구간합
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))  #N개의 정수 리스트
    result = []  # 리스트를 만들고 리스트 안의 값을 통해 보여줄 것
    ans = []  #최대 - 최소
    for i in range(N-M+1): #범위가 index값을 벗어나지 않도록 N에서 -M을 해줌.
        result.append(sum(arr[i:i+M]))
    ans = max(result) - min(result)
    print(f'#{tc}', ans)