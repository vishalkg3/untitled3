def main():
    n1 = int(input("ENter no of words"))
    w1 = []
    ct1=[]
    for i in range(0, n1):
        w1.append(input("Enter word"))
    print(w1)
    print(len(w1))
    w1.sort()
    print(w1)
    j=0
    while j < len(w1):
        print("\nValue of j at start of loop = ", j )
        print(w1[j])
        ct1.append(w1.count(w1[j]))
        j=j+w1.count(w1[j])

        print("\nValue of j at end of loop = ", j)


       # print(w1[j])

        #for k in range(j+1,len(w1)):
        #    if(w1[j]==w1[k]):
        #        print("Words matched")
        #        print(w1[j],w1[k])
        #        j=k
        #    else:
        #        j=j+1


    print(w1)
    print(ct1)
    print(len(ct1))
    ct1.sort(reverse=True)
    print(ct1)
if __name__ == '__main__':
    main()
