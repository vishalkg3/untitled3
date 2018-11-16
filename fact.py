count=0
num = int(input())
f = 1
if num <1 or num>1000:
    exit()
for i in range(1, num + 1):
    f = i * f
#print(f)
d = str(f)
#print(d[-1])
#print(d[0])
k = -1
for l in range(int(len(d))):
    if d[k] != '0' :
     #   print("exiti")
        break
    k=-1-l
    #print(k)
    print(d[k])
    #k = k - l
    count+=1
    #print("curret",count)



print(count-1)
