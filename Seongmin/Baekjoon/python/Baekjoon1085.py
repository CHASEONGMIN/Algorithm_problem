#백준 1085 직사각형에서 탈출 브3

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))
