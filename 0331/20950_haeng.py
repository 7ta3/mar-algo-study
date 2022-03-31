def find(x,I):
    global result
    if x > 7:
        return
    if x >= 2:
        diff= abs(ST[0]//x-gom[0])+abs(ST[1]//x-gom[1])+abs(ST[2]//x-gom[2])
        if diff < result:
            result = diff
    for i in range(I,N):
        ST[0] += Nlist[i][0]
        ST[1] += Nlist[i][1]
        ST[2] += Nlist[i][2]
        find(x+1,i+1)
        ST[0] -= Nlist[i][0]
        ST[1] -= Nlist[i][1]
        ST[2] -= Nlist[i][2]

N=int(input())
Nlist=[]
for _ in range(N):
    Nlist.append(list(map(int,input().split())))
gom=list(map(int,input().split()))

result=9999999999
ST=[0,0,0]
find(0,0)

print(result)

