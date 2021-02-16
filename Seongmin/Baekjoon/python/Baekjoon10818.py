N = int(input())
arr = list(map(int, input().split()))
max = arr[0]
min = arr[0]
for i in arr:
    if max < i:
        max = i
    elif min > i:
        min = i
print(min, max)