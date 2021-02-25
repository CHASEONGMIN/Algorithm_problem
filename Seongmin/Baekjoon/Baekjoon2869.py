#백준 2869 달팽이는 올라가고 싶다 브1

A, B, V = map(int, input().split()) #올, 미, 높
cnt = 0
height = V - B #마지막에는 A만큼 올라가므로
if height % (A - B) != 0:
    cnt = ((height)//(A-B)) + 1
else:
    cnt = ((height) // (A-B))
print(cnt)


#시간초과 조심
# A, B, V = map(int, input().split()) #올, 미 , 높
# cnt = 0
# while V > 0:
#     cnt += 1
#     V = V - A
#     if V > 0:
#         V = V + B
#         continue
#
# print(cnt)

