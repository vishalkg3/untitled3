def unique(list3):
    list4=[]
    list1=sorted(list3)
    i=0
    while i < len(list1):
        count=list1.count(list1[i])
        list4.append(list1[i])
        if count > 1:
            i+=count
        else:
            i+=1
    return list4
list5=[]
num=int(input())
if num>100 or num<1:
    exit()

nodes=list(map(int, input().split()))
if num!=len(nodes):
    exit()
if not nodes.count(-1) ==1 :
    exit()


for check in nodes:
    if check >= num-1 or check <-1:
        exit()
remove=int(input())
if remove>=num or remove<0:
    exit()

a=sorted(nodes)

i = 1
s = {}
z=unique(a[1:])
y=list(range(0,len(a)))
u=[]

for x in y:
    if not x in z:
        u.append(x)
#print("All the leaf nodes ---> ",u)
sing=[]
while i < len(a):

   # print("\nCount of {} is {}  ".format(a[i], a.count(a[i])))
   # print("All the nodes of {} ".format( a[i]))
    k = i
    for j in range(0, a.count(a[i])):

       # print(k, end=" ")
        if j == 0:
            s[a[i]] = [k]
        else:
            s[a[i]].append(k)

        if a.count(a[i]) == 1:
            #print("\n {} is single leaf (no sibling) \n".format(k))
            sing.append(k)
        k += 1
   # print('\n')
    i += a.count(a[i])

#print("\n\n",s)
list2=[]
#r = int(input("Enter node to be removed - \n"))
r=remove
#print("we want node {} to be removed \n".format(r))
if r in u:
    print(len(u)-1)
    exit()
#for b in y:
for b in s.keys():
    #print("valuee   = ", b)
    if r == b:
        list2.append(r)
        #print("{} node found in keys ".format(b))
        for c in s[b]:
   #         print("Value of c ",c)
            #del s[c]
            list2.append(c)
            for m in list2:
                if m in s.keys():
                    for n in s[m]:
                        list2.append(n)
    #                    print(list2)


#print("List -----> ", unique(sorted(list2)))

q=[]
for v in u:
    if not v in unique(sorted(list2)):
        q.append(v)

#print(q)
ans=len(q)
#print("All single leaves  ", sing)

if remove in sing:
    #print("No of leave after remove {} node from tree is {}".format(remove, ans+1))
    print(ans+1)
else:
    #print("No of leave after   remove {} node from tree is {}".format(remove, ans ))
    print(ans)