another=[]
diff=[]
def calculateMin(sL, kfact):
    another=sorted(sL, reverse=True)
    print(another)
    for j in range(len(sL)/2):
        print(another[j], another[-1-j])

T=int(input())

for i in range(T):
    tn, k  = map(int, input().split())
    shopList=list(map(int, input().split()))
    print(tn, shopList, k)
    if len(shopList)%2!=0 or len(shopList)!=tn or T<1 or T>50 or tn <2 or tn > 1000000 or k <0 or k > 1000000:
        exit()
    calculateMin(shopList, k)

