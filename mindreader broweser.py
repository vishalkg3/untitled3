fract={}
def wordCalc(strng):
    newStng=strng[4:-4]
    mind=[]
    for j in newStng:
        if j not in 'aeiou':
            mind.append(j)

    fract[len(strng)]=len(mind)+4
    print(fract)

N=int(input())
if N<1 or N>100:
    exit()

for i in range(N):
    url=input()
    #print(url[0:4], url[-4:])
    if url[0:4] != "www." or url[-4:] != ".com" or len(url)>200:
        #print("exiting.......")
        exit()
    wordCalc(url)
    #print(result)
print(fract)