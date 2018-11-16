
testCase=int(input())
mainlist=[]
#def minReturn(n,list1):
if testCase<1 or testCase>10**5:
    exit()


for sz in range(testCase):
    arraySize=int(input())
    if arraySize<2 or arraySize>10**5:
        exit()
    nodes=list(map(int, input().split()))
    if arraySize != len(nodes):
        exit()

#print(nodes)
    minList=[]
    for i in range(len(nodes)):
        sumLeft = 0
        sumRight = 0
    #print(nodes[i],i)
        for k in range(i+1):
        #print("value of k is {}".format(k))
            sumLeft+=nodes[k]
        #print("nodes K ",nodes[k])
        for l in range(i+1,len(nodes)):
        #print("value of l is {}".format(l))
            sumRight+=nodes[l]
        #print("nodes L ",nodes[l])

   # print("Sum from left is {} \n And sum from right is {}".format(sumLeft,sumRight))
        minList.append(sumRight-sumLeft)
    try:
        #print(min([n for n in minList if n>=0]))
        mainlist.append(min([n for n in minList if n>=0]))
    except ValueError:
        print("-1")
for s in mainlist:
    print(s)
