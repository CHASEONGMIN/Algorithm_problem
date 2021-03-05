#백준 11653 소인수분해 실4

N = int(input())

while N > 1:
    for i in range(2, N+1):
        while N % i == False:
            if N % i == 0:
                print(i)
                N = N // i



