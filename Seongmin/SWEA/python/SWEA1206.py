#SWEA 1206

for tc in range(1, 11):
    N=int(input())
    arr=list(map(int, input().split())) #인덱스로 활용
    result = 0

    for i in range(2, N-2):
        # 좌측 2개, 우측 2개 중 가장 큰 빌딩을 찾고, 그 빌딩과의 비교를 통해 계산
        arr2 = max(arr[i+1], arr[i+2], arr[i-1], arr[i-2])
        if arr[i] > arr2:
            result += arr[i] - arr2

    #조망권이 확보된 세대수를 계산
    print("#{} {}".format(tc,result))
