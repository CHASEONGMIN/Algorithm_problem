#백준 1193 브2
#규칙찾기가 어려움
# 홀 : 분자는 n to 1, 분모 1 to n
# 짝 : 분자는 1 to n, 분모 n to 1

num = int(input())
idx = 0
while True: #num에서 idx로 1,2,3,..을 빼며 몇 번째 그룹인지 파악
    idx += 1
    num -= idx
    if num <= 0: #num은 0보다 작거나 같은수가 되기 직전의 수로 되돌려줘야 함.
        # -> idx:그룹의 분모와 분자의 합, num은 그룹에서 몇번째 수인지 알 수 있음.
	    num += idx
	    idx += 1
	    break

if idx%2==0:
	print((idx - num), '/', num, sep='')
else:
	print(num, '/', (idx - num), sep='')