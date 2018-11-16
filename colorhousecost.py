N=int(input())
street=[]
for i in range(N):
    house = list(map(int, input().split()))
    #print("house  ", house)
    street.append(house)


print(street)
for j in range(N):
    p=street[j].index(min(street[j]))
    m=min(street[j])
    print(p)
    new=[x for x in street[j] if x!=m]
    print("New for " , j , " " , new)
    print("COst j : " ,min(new))