#백준 1676 팩토리얼 0의 개수 S4
#5로 나눈 것의 몫만큼 더해주면 됨.

n = int(input())
cnt = 0

while n >= 5:
    cnt += n//5
    n //= 5

print(cnt)