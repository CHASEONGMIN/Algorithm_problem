#백준 10872 팩토리얼 B3
#쉽지만 기본적인거라 중요

def fac(n):
    if n<= 1:
        return 1
    else:
        return n * fac(n-1)

N = int(input())
print(fac(N))
