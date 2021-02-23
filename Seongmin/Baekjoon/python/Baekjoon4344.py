#평균은 넘겠지
#리스트를 받아오고 슬라이싱을 통해 나눈다
# 슬라이싱 관련 좋은 문제


C = int(input())
for _ in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0] # 슬라이싱을 이용한 평균

    cnt = 0
    for i in nums[1:]: #점수들 중
        if i > avg:
            cnt += 1
    percent = cnt/nums[0] * 100
    print(f'{percent:.3f}%')