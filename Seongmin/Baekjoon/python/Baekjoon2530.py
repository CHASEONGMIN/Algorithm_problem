#백준 2530 인공지능 시계

A, B, C = map(int, input().split())
D = int(input())

C += D % 60
D = D // 60
if C >= 60:
    C -= 60
    B += 1

B += D % 60
D = D // 60
if B >= 60:
    B -= 60
    A += 1

A += D % 24
if A >= 24:
    A -= 24

print(A, B, C)