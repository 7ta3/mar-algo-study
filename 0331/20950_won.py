# 틀린 코드입니당

n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]
gom = list(map(int, input().split()))

if n > 7:
    n = 7
def f(x, arr, c, diff):
    global minV
    if minV < diff:
        return
    if x == n:
        if c >= 2:
            minV = min(minV, diff)
        return
    tmp = arr[:]
    tmp = list(map(lambda x: x * c, tmp))
    for i in range(3):
        tmp[i] += color[x][i]
    tmp = list(map(lambda x: x // (c + 1), tmp))
    diff = 0
    for i in range(3):
        diff += abs(tmp[i] - gom[i])
    f(x + 1, tmp, c + 1, diff)
    diff = 0
    for i in range(3):
        diff += abs(arr[i] - gom[i])
    f(x + 1, arr, c, diff)

minV = 255 * 3
f(0, [0, 0, 0], 0, 0)
print(int(minV))
