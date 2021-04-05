#백준 1436 영화감독 숌 S5
#브루트포스 문제

N = int(input())

str1 = 666  # 첫번쨰 값인 666부터 시작
cnt = 0

while True:
    if '666' in str(str1): # in을 쓰기 위해 str로
        cnt += 1
        if cnt == N:
            print(str1)
            break
    str1 += 1