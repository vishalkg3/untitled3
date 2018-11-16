strng3=input()
#print(strng)
if not strng3.islower() or len(strng3)>100000 :
    exit()

ntpalin=[]


def isPalindrome(strng2):
    cnt=0
    for k in range(int(len(strng2)/2)):
        #print(k)
        if strng2[k] == strng2[len(strng2)-k-1]:
            #print("char {} and char {} matched " .format(strng2[k],  strng2[len(strng2)-k-1]))
            cnt+=1
            #print("current count",cnt)
        else:
            break
   # print("value of count",cnt)
    if cnt==int(len(strng2)/2):
       # print("{} is a palindrome".format(strng2))
        return 0

#print("half lenght" ,int(len(strng)/2))
#a=isPalindrome(strng)
#print(a)



for j in range(len(strng3)+1):
    for i in range(j,len(strng3)):
        a=isPalindrome(strng3[j:i+1])
        if a!=0:
            #print(strng3[j:i+1],"noot")
            ntpalin.append(strng3[j:i+1])
#print(ntpalin)
try:
    print(len(max(ntpalin,key=len)))
except ValueError:
    exit()