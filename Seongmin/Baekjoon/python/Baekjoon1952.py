#백준 1952 달팽이2 브3

m, n = map(int,input().split())
arr = [[0] * n for _ in range(m)]
# 우하좌상
direct = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}

end = m*n-2
cnt = 0
h = 0
i,j = 0,0
arr[i][j] = "1"
while end>=0:
    complete = False
    if 0<=i+direct[h][0]<m and 0<=j+direct[h][1]<n:
        if arr[i+direct[h][0]][j+direct[h][1]] != "1":
            arr[i+direct[h][0]][j+direct[h][1]] = "1"
            i,j = i+direct[h][0],j+direct[h][1]
            complete = True
    if not complete:
        cnt += 1
        h = (h+1)%4
        i,j = i+direct[h][0],j+direct[h][1]
        arr[i][j] = "1"
    end -= 1
print(cnt)


#########간단한 풀이
# m,n=map(int,input().split())
# x=n
# y=m-1
# count=0
# while True:
#     if y==0:
#         break
#     count+=1
#     x-=1
#     if x==0:
#         break
#     count+=1
#     y-=1
# print(count)