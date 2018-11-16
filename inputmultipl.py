list5=[]
num=int(input())
nodes=list(map(int, input().split()))
if num==len(nodes):
    print("gooood")
else:
    print("not goooood")
    exit()
remove=input()

print(num, nodes, remove)
a=sorted(nodes)