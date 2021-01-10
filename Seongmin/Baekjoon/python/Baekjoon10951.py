while True:
    try:
        A , B = map(int, input().split())  # (0 < A, B < 10)
        print(A + B)
        continue

    except:
        break