def makecombi(get_,loc,combi):
    global nums, n, colors, gomduri,answer
    if 1 < loc <= min(n,7):
        result = 0
        for i in range(3):
            result += abs((combi[i]//loc)-gomduri[i])
        if answer > result:
            answer = result
        if loc == min(n,7):
            return
    for idx in range(get_,n):
        if nums[idx] == 0:
            nums[idx] = 1
            makecombi(idx,loc+1,[combi[0]+colors[idx][0],combi[1]+colors[idx][1],combi[2]+colors[idx][2]])
            nums[idx] = 0

n = int(input())
colors = [list(map(int,input().split())) for _ in range(n)]
gomduri = list(map(int,input().split()))
nums = [0]*n
answer = 255*3
makecombi(0,0,[0,0,0])
print(answer)
