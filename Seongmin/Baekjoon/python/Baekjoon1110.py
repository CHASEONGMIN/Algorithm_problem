#백준 1110번 더하기 사이클 브1

num = int(input())

chk = num #체크용으로 하나 만들어 줘야 함.
n_num = 0
temp = 0
res = 0
while True:
    temp = num//10 + num%10  #십의 자리수  + 일의 자리수
    n_num = (num%10)*10 + temp%10
    res += 1
    num = n_num
    if n_num == chk:
        break
print(res)