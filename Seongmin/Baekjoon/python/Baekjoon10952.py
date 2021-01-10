while True:
    A, B = map(int, input().split())  # (0 < A, B < 10)
    if A == 0 and B == 0:
        break
    print(A + B)