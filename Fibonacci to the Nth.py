
x = 1

a = 0
b = 1
c = 1

if x == 1:
    print (a)
    exit()
elif x==2:
    print (b)
    exit()
elif x==3:
    print (c)
    exit()
elif x>3:
    while x>3:
        a = b
        b = c
        c = a+b
        x = x-1
print (c)        