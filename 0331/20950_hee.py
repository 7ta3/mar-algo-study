def Munduri(idx, K, R, G, B):
    global ans
    if K > 1:
        r, g, b = gomduri
        rr, gg, bb = R // K, G // K, B // K
        ans = min(abs(r-rr) + abs(g-gg) + abs(b-bb), ans)
    # 혼합한 RGB 값 체크

    if K == 7:
        return
    # 최대 7개의 색만을 혼합할 수 있다

    for i in range(idx, N):   
        r, g, b = arr[i]
        Munduri(i+1, K+1, R + r, G + g, B + b)

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
gomduri = list(map(int, input().split()))
ans = 255 + 255 + 255

Munduri(0, 0, 0, 0, 0)
print(ans)
