#백준 2775 부녀회장이 될테야 브2
#같은 층 i+1호는 i호의 인원에 k-1층 i+1호의 인원만큼 데리고 살면되므로

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    people =[ i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            people[j] += people[j-1]
    print(people[-1])
