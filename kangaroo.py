
count=[]

def kang(strt, stop, hop):
    k=0
    for i in range(strt,stop+1):
        if i%hop==0:
            k+=1
    count.append(k)


N=int(input())
if N<1 or N>100000:
    exit()
for j in range(N):
    a,b,c=map(int, input().split())
    if a<1 or b<1 or a>b or c<1 or a>10**12 or b > 10**12 or c > 10**12  :
        exit()
    kang(a,b,c)

for l in count:
    print(l)