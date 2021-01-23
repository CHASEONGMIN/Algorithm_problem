T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    ans = a // b
    ans2 = a % b
    print(f'#{tc} {ans} {ans2}')


