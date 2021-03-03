#백준 2525 오븐 시계 브4
A, B = map(int, input().split())
C = int(input())

A += C // 60 #시
B += C % 60 #분

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print('%d %d' % (A ,B))