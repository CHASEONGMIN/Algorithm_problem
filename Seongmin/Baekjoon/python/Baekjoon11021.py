a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    #sum = b + c 로도 가능
    print("Case #%s: %s" %(i+1, (b+c)))