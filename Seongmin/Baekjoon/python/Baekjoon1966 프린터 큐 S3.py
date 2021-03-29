#백준 1966 프린터 큐 S3
# 큐 활용해서 풀어 봄

for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = list(map(int, input().split())) #문서 리스트를 큐로 생성

    # N크기짜리 리스트 생성 후 M번째 인덱스 위치에 1 넣어주고 두개의 리스트 이용
    idx_arr = [0 for _ in range(N)]
    idx_arr[M] = 1

    cnt = 0
    while queue:
        if queue[0] == max(queue):
            cnt += 1
            if idx_arr[0] == 1:
                print(cnt)
                break
            else:
                queue.pop(0)
                idx_arr.pop(0)
        else:
            queue.append(queue.pop(0))
            idx_arr.append(idx_arr.pop(0))
