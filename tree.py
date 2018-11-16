#rtList=[-1,0,0,1,1,1,2,2,3,3,4,4,5,5,5]
rtList=[-1,0,0]
#print(len(rtList))
a={0:{1:{3:{8:{},9:{}},4:{10:{},11:{}},5:{11:{},12:{},13:{}}},2:{6:{},7:{}}} }
#print(a[0][1][4][10])
#print(len(a[0][1]))
p=0
while p < 10:
    for key in a:
        print(key)
    print(type(a))
    l={}
    a="a["+str(key)+"]"
    print(type(a))
    a="".join(a)
    print("After Join =  ",a)
    #dict()
    print(type(a))

    #dict(a)
    print(a)
    p+=1
b={0:{}}
b[0]={1:{}}
#print(b)
b[0].update({2:{}})
#print(b)

b[0][1].update({3:{}})
b[0][1][3].update({7:{}})
#print(b)
c={0:{}}
for i in range(1,len(rtList)):
    c[rtList[i]].update({i:{}})


    #print(c)

