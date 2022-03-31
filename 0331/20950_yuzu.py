def dfs(depth, x, sr, sg, sb):
    global ans
    if depth == dd:
        res = abs(r-(sr//depth))+abs(g-(sg//depth))+abs(b-(sb//depth))
        if ans > res:
            ans = res
        return
    for i in range(x, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth+1, i, sr+arr[i][0], sg+arr[i][1], sb+arr[i][2])
            visited[i] = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, g, b = map(int, input().split())
visited = [0]*n
if n >7:
    d = 7
else:
    d = n
ans = 10**9
for dd in range(2, d+1):
    dfs(0, 0, 0, 0, 0)
print(ans)