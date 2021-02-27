#백준 1065 실4
#key 1~99는 모두 한수라는 점. 각 자리수별로 분리하기 위해 map활용을 한다는 것

N = int(input())
res = 0

for n in range(1, N + 1):
    if n <= 99:  # 1부터 99까지는 모두 한수
        res += 1

    else:
        nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
        if (nums[0] - nums[1]) == (nums[1] - nums[2]):  # 등차수열 확인
            res += 1
print(res)