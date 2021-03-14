#백준 11050 이항 게수 B1
#이항계수에 대한 이해가 더 필요

N, K = map(int, input().split())

fac = [1 for _ in range(N+1)] #각 자리수만큼 리스트 만들어 줌

for i in range(1, N+1):
    fac[i] = i * fac[i-1]

print(fac[N]//fac[N-K]//fac[K])  #N! / (N-K)! K!


