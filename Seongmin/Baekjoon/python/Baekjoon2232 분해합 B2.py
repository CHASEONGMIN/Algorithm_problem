#백준 2232 분해합 B2
#어려움 브루트포스 문제
# 1부터 입력받은 num까지의 숫자중에서 분해합을 했을때 num이 되면 그 값을 출력
# 상황에 맞는 변수 생성 및 활용 중요

def brute(num):
    total = num
    while True:
        if num <= 0:
            break
        total += num % 10
        num = num // 10
    return total

num = int(input())
res = 0

for i in range(1, num + 1):
    temp = brute(i)
    if temp == num:
        res = i
        break
if res == 0:  #생성자가 없는 경우
    print(0)
else:       #생성자가 있는 경우
    print(res)  
