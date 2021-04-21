#백준 2003 수들의 합2 S3
#더블 포인터 활용

import sys
sys.stdin = open('text/2003.txt', 'r')

n, m = map(int, input().split()) #n개의 수로된 수열, i~j까지의 합이 m이되는 것의 개수 구하기
arr = list(map(int, input().split())) # n개의 수 수열
cnt = 0
l, r = 0, 1 #포인터 설정

temp = arr[l] #임시 리스트 생성해주고 여기에 값  넣어주면서 계산

while l < n:
    if temp == m:  #값이 m이되면 cnt 증가시키고 좌측 포인터를 1증가시키고 임시 리스트에서 가장 좌측 값을 빼줌
        cnt += 1
        temp -= arr[l]
        l += 1

    if r == n and temp < m: #끝에까지 갔음에도 m보다 적으면 break
        break

    if temp < m:  #값이 m보다 작으면 우측 한칸더 추가해서 값 더해줌
        temp += arr[r]
        r += 1

    if temp > m: #값이 m보다 크면 제일 좌측을 빼서 값을 조정
        temp -= arr[l]
        l += 1

print(cnt)
