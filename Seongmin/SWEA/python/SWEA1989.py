T = int(input())
for tc in range(1, T + 1):
    word = str(input())
    ans = 1
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            ans = 0
            break
    print(f'#{tc} {ans}')


