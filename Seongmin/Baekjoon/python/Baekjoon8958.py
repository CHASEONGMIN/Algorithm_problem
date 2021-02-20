n = int(input())

for i in range(n):
    res = 0
    sum = 0
    ox = input()
    for j in range(len(ox)):
        if ox[j] == 'O':
            sum += 1
            res += sum
        elif ox[j] == 'X':
            res += 0
            sum = 0
    print(res)

