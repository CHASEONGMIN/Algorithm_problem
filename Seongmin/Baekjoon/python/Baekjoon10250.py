#백준 10250 ACM 호텔 브3

for _ in range(int(input())):
    H,W,N = map(int, input().split())
    i = N % H # 몇 층
    j = N // H+1 # 몇 호
    if i == 0: #트기 케이스 처리 해줌.
        i = H
        j -= 1
    print(i * 100 + j)