#백준 1890 수들의 합 S5
#1부터 N까지의 합이 S보다 커지면 N-1출력하면 끝

N = int(input())
i = 1
while i * (i + 1) / 2 <= N:
    i += 1
print(i - 1)