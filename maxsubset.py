N=int(input())
origList=list(map(int, input().split()))
final=[]
#print(N, origList)
if N != len(origList) or N<1 or N> 100000:
    exit()

st=sorted(origList, reverse=True)
#print(st)
for j in range(len(st)):
    if st[j]<1 or st[j]>1000000:
        exit()
    #print(st[j], "is evolving. \nIt will evolve on", j+st[j]+1 ,"day")
    final.append(j+st[j]+1)
#print(final)
a=max(final)
print(a+1)
