'''
별 찍기 - 3

n = int(input())
for i in range(n, 0, -1):
    print(('*' * i))

별 찍기 - 4

n = int(input())
for i in range(n, 0, -1):
    print((' ' * (n-i) + '*' * i))

별 찍기 - 5 (우측 공백 없네)

n = int(input())
for i in range(1, n+1):
    print((' ' * (n - i) + ('*' * (2 * i - 1))))

별 찍기 - 6

n = int(input())
for i in range(n, 0, -1):
    print((' ' * (n - i) + ('*' * (2 * i - 1))))

별 찍기 - 7

n = int(input())

for i in range(1, n+1):
    print((' ' * (n - i) + ('*' * (2 * i - 1))))

for i in range(n-1, 0, -1):
    print((' ' * (n - i) + ('*' * (2 * i - 1))))

별 찍기 - 8

n = int(input())

for i in range(1, n+1):
    print(('*' * i) + (' ' * 2 * (n - i) + ('*' * i)))

for i in range(n-1, 0, -1):
    print(('*' * i) + (' ' * 2 * (n - i) + ('*' * i)))

별 찍기 - 9

n = int(input())

for i in range(1, n+1):
    print((' ' * (i-1)) + ('*' * ((2 * (n - i) + 1))))

for i in range(n-1, 0, -1):
    print((' ' * (i-1)) + ('*' * ((2 * (n - i) + 1))))

별 찍기 - 10

def star(n):
    global Arr

    if n == 3: # 첫 케이스 설정
        Arr[0][:3] = Arr[2][:3] = [1] * 3
        Arr[1][:3] = [1, 0, 1]
        return

    num = n // 3
    star(n // 3)
    for i in range(3):
        for j in range(3): # 구간 나눔
            if i == 1 and j == 1: # 첫 케이스이니까 바꿔줄 필요가 없음.
                continue
            for k in range(num):
                Arr[num * i + k][num * j:num * (j + 1)] = Arr[k][:num]  # 가장 중요한 부분


N = int(input())

# 메인 데이터 선언
Arr = [[0 for i in range(N)] for i in range(N)]

star(N)

for i in Arr:
    for j in i: # 1이면 *을, 0이면 공백을 입력
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

'''