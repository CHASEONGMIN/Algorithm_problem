#백준 11720 숫자의 합 브2
N = int(input()) # 숫자의 개수
M = map(str, input())
sum = 0
for i in M:
    sum += int(i)
print(sum)
