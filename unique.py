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



