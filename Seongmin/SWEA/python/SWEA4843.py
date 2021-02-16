#SWEA4843 특별한 정렬
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = sorted(list(map(int, input().split()))) #오름차순 정렬
    length = len(arr)
    a = []
    b = []
    res = []

    #홀수 짝수로 나눠서 리스트 만들어 줌
    for i in range(length):
        if i < (length // 2):
            a.append(arr[i])
        elif i > (length // 2) - 1:
            b.append(arr[i])
    b.sort(reverse=True) #내림차순 정렬

    for i in range(5): #10개 출력을 위해 10개만
        res.append(b[i])
        res.append(a[i])


    print("#{} {}".format(tc," ".join(map(str, res))))


# 풀이2 인덱스 활용
import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     num_lst = list(map(int, input().split()))
#     result_lst = []
#     for i in range(10):  # 10개만 출력
#         max_num, min_num = num_lst[0], num_lst[0]  # 첫 항을 최대 최소로 설정
#         idx = 0
#         if i % 2 == 0:  # 최대값의 index 검출
#             for j in range(len(num_lst)):
#                 if num_lst[j] >= max_num:
#                     max_num = num_lst[j]
#                     idx = j
#         else:  # 최소값값의 index 검출
#             for j in range(len(num_lst)):
#                 if num_lst[j] <= min_num:
#                     min_num = num_lst[j]
#                     idx = j
#
#         result_lst.append(num_lst.pop(idx))  # num_lst.pop -> result_lst
#
#     print('#{} '.format(test_case) + ' '.join(map(str, result_lst)))
