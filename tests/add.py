import cin

s = 0
x = cin.scan(int)
while x is not None:
    s += x
    x = cin.scan(int)
print(s)
