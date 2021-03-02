#백준 2447 별 찍기 - 10 실1
# 구간 나누기 및 재귀함수 활용
# 중요 복습 필요

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

