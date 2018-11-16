def camelcase(s):
    a=1
    for i in range(len(s)):
        if s[i].isupper():
            a = a + 1
    return a
if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
