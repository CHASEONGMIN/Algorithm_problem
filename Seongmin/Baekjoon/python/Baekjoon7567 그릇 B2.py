#백준 7567 그릇 B2

bracket = input()
sum = 10
for x in range(len(bracket) -1):
    if bracket[x] == bracket[x+1]:
        sum += 5
    else:
        sum += 10
print(sum)
