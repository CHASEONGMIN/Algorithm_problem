#백준 11557 Yangjojang of The Year S5

T = int(input())
for _ in range(T):
    A_a, B_b = A, B = 0, 0
    for _ in range(int(input())):
        A, B = map(str, input().split())
        if int(B) > int(B_b):
            A_a, B_b = A, B
        else:
            continue
    print(A_a)

