a = int(input())
cnt = 0

for i in range(1, a+1):
    if(a % i==0):
        cnt += 1
        print("{}(은)는 {}의 약수입니다.".format(i, a))


if(cnt == 2):
    print("{}(은)는 1과 {}로만 나눌 수 있는 소수입니다.".format(a, a))

