startCount=[]
def startMatrix():
    N=int(input())
    starfound=[]

    t1=0
    t2=0
    if N<3 or N>20 or N%2==0:
        exit()
    centre=int((N+1)/2)
   # print("Desired value of star  " , centre , centre)
    for i in range(N):
        matrow=input()
        if len(matrow)!=N or matrow.count('*')>1 or :
            exit()
        if '*' in matrow:
            t1=abs(matrow.index('*')+1-centre)
            starfound.append(i+1)
    #print(starfound)
    if len(starfound)!=1:
        exit()
    t2=abs(starfound[0]-centre)
    startCount.append(t1+t2)

T=int(input())
if T>50 or T<1:
    exit()
for i in range(T):
    startMatrix()
for k in startCount:
    print(k)