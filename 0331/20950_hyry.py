# -------------------------- 1

import sys
input = sys.stdin.readline

def comb(depth, max_depth, start, sumR, sumG, sumB):
    global mindiff

    if depth == max_depth:
        newR = int(sumR / depth)
        newG = int(sumG / depth)
        newB = int(sumB / depth)
        diff = abs(gR - newR) + abs(gG - newG) + abs(gB - newB)
        if mindiff > diff:
            mindiff = diff
        return

    for color in range(start, N):  # 0번부터 N - 1번 물감
        if not used[color]:
            result[depth] = color
            used[color] = True
            comb(depth + 1, max_depth, color, sumR + colors[color][0], sumG + colors[color][1], sumB + colors[color][2])
            used[color] = False



N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
gR, gG, gB = map(int, input().split())
used = [False] * N
max_depths = N if N <= 7 else 7
mindiff = 1e10

for max_depth in range(2, max_depths + 1):
    result = [-1] * max_depth
    comb(0, max_depth, 0, 0, 0, 0)

print(mindiff)

# ----------------------- 2
import sys
from itertools import combinations as co
input = sys.stdin.readline

N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
gR, gG, gB = map(int, input().split())
max_depths = N if N <= 7 else 7
mindiff = 1e10

for max_depth in range(2, max_depths + 1):
    for co_set in co(range(N), max_depth):
        newR = newG = newB = 0
        for i in co_set:
            newR += colors[i][0]
            newG += colors[i][1]
            newB += colors[i][2]

        diff = abs(gR - int(newR/max_depth)) + abs(gG - int(newG/max_depth)) + abs(gB - int(newB/max_depth))
        if mindiff > diff:
            mindiff = diff

print(mindiff)
