boyList=list(map(int, input().split()))
girlList=list(map(int, input().split()))
counterBoy=[]
pairBoy=[]
counterGirl=[]
pairGirl=[]
def fight(bList, gList):
    for i in range(1, len(bList)+1):
        print("Boy no. " , i , " likes girl no. ", bList[i-1])
        print("But girl ", bList[i-1], " likes boy no ", gList[bList[i-1]-1])
        #print("Girl no. ", i, " likes boy no. ", gList[i-1])
        if(i!=gList[bList[i-1]-1]):
            print("Boy no " , i , " beats up " , gList[bList[i-1]-1])
            counterBoy.append(gList[bList[i-1]-1])
            pairBoy.append([i,gList[bList[i-1]-1] ])
    for i in range(1, len(bList)+1):
        print("girl no. " , i , " likes boy no. ", gList[i-1])
        print("But boy ", gList[i-1], " likes girl no ", bList[gList[i-1]-1])
        #print("Girl no. ", i, " likes boy no. ", gList[i-1])
        if(i!=gList[bList[i-1]-1]):
            print("Girl no " , i , " beats up " , gList[bList[i-1]-1])
            counterGirl.append(gList[bList[i-1]-1])
            pairGirl.append([i,gList[bList[i-1]-1] ])

fight(boyList, girlList)
print(counterBoy, counterGirl)
print(pairBoy, pairGirl)