'''
T = n개

for testcase in range(T):
    nums = input()
    print(nums)

a = input() #'3 3'
a.split() # ['3', '3']
map(a.split(), int) # [3, 3]

import sys
sys.stdin = open("input.txt", "r")
'''




T = int(input()) #첫번째

for tc in range(1, T+1):
    #각 테스트 케이스에 대한 입력
    nums = map(int, input().split())
    
    #Main logic
    total = 0    
    for num in nums:
        if num % 2 == 1:
            total += num        
    print(f'#{tc}', total)