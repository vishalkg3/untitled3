N=int(input())
if N<1 or N>100:
    exit()
passList=[]
palList=[]
for i in range(N):
    passList.append(input())
#print(passList)

def Reverse(pwd):
    revStrng=pwd[::-1]
    return revStrng

m=1
for j in passList:
    if len(j)%2==0 or len(j)<3 or len(j)>13 or ' ' in j:
        print("exitt")
        exit()
    result=Reverse(j)

    for k in passList[m:]:
        if k==result:
            palList.append(k)
           # print(k, " : reverse exist")
    m+=1


if len(palList)>1:
    exit()
else:
    n=len(palList[0])
    print(n, palList[0][int(n/2)])