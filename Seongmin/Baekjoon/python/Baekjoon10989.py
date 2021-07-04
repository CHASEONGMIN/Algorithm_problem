import sys
n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)
'''
내 작성 코드 (메모리 초과)

import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

k = max(arr)
count = [0] * (k+1)
res = [0 for _ in range(len(arr))] # 항목의 개수만큼

for i in arr: #A의 원소 count
    count[i] += 1 #원소의 값에 맞는 counter의 해당 인덱스 값을 +1

for i in range(len(count)-1):
    count[i+1] += count[i]  #누적 count

for i in range(len(arr)-1, -1, -1):
    res[count[arr[i]] -1] = arr[i]
    count[arr[i]] -=1

for i in range(len(res)):
    print(res[i])
'''
