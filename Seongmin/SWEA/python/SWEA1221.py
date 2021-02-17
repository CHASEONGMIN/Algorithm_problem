#SWEA 1221 GNS
import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())  #테스트 케이스의 개수

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"] #미리 정렬을 시킨 num 준비


for tc in range(1, 1 + T):

    n = list(map(str, input().split()))

    new_str = list(map(str, input().split()))  # 무작위 문자열을 리스트로
    ans = [] # 결과 저장용

    for i in range(10):   #zro부터 nin까지 10개 이므로 10으로 해주어야 함.
        for j in new_str:   #리스트로 만든 문자열들 중에
            if num[i] == j:  #num이 정렬이 되어 있기 때문에 같은 값이 보이면 추가해주면 끝
                ans.append(j)  #zro zro zro..이렇게 누적 됨.

    print(n[0])
    print(*ans)