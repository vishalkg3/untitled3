b = open("G:/abc.txt", 'r')
c = open("G:/abc.txt", 'r')
# print(b.read())
print("first line of b\n" + b.readline())
print("first line of c\n", c.readline())
print("second line of b\n", b.readline())
print("second line of c\n", c.readline())
print("remaining  lines of c\n", c.readlines())
print("third line of b\n", b.readline())
print("remaining  lines of c\n", b.readlines())
# print(b.readlines())
a = b.read()
print(a)
