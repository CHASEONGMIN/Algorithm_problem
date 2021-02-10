#SWEA 1208 Flatten
import sys
sys.stdin = open('input.txt', 'r')

for i in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    result = 0
    while dump: #최대 위치값 감소와 최소 위치 값 증가를 덤프가 0이 될때까지 계속 진행한다.
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
        dump -= 1
    #결과값 출력
    result = max(box) - min(box)
    print("#{} {}".format(i, result))
