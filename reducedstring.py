def super_reduced_string(s):
    # Complete this function
    s=list(s)
    i=0
    s1=len(s)-1
    while i < s1:
        if (s[i] == s[i+1]):
            del s[i+1] , s[i]
            i=0
            s1 = len(s) - 1
        else:
            i+=1
    if len(s) == 0:
        s="Empty String"
    return ''.join(s)
s = input().strip()
result = super_reduced_string(s)
print(result)
