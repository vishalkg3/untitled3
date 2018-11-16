try:
    num=int(input())
except ValueError:
    exit()
maxlist=[]
list1=list(map(int, input().split()))
if num != len(list1) or num<1 or num>200000:
    exit()

for m in list1:
    if m > 100000 or m < -100000 or m==0:
        exit()
def checkBalance(list3):
    #print(list3)
    cnt = 0

    for k in range(int(len(list3) / 2)):
         #print(k)
         if 0 in list3:
             break
         if list3[k] == list3[(len(list3) - k - 1)]*-1:
             #print("char {} and char {} matched " .format(list3[k],  list3[len(list3)-k-1]))
             cnt += 1
             #print("current count",cnt)
         else:
            break
   # print("value of count",cnt)
    if cnt == int(len(list3) / 2):
        #print("{} is a palindrome".format(list3))
        maxlist.append(list3)

        return 0

for j in range(len(list1)+1):
    for i in range(j,len(list1)):
        if len(list1[j:i+1])%2==0:
            checkBalance(list1[j:i+1])

try:
    print(len(max(maxlist,key=len)))
except ValueError:
    exit()