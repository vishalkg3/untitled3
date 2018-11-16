str=input()
for j in range(len(str)+1):
    for i in range(j,len(str)):
        print(str[j:i+1])

