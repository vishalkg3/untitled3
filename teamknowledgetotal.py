test=int(input())
if test<1 or test>100:
    exit()
for i in range(test):
    list1=list(map(int, input().split()))
    if list1[0] < 1 or list1[0] >100:
        exit()
    for q in range(len(list1)):
        if list1[q]<0 or list1[q]>10000:
            exit()
    slist=sorted(list1[1:])
    if list1[0] != len(slist) or len(slist)%2!=0:
        exit()

    maxKnow=slist[0]+slist[-1]
    minKnow=slist[int((len(slist)/2)-1)]+slist[int((len(slist)/2))]
    print(maxKnow-minKnow)