a,b = 0,1
for i in range(0,10):
    a,b = b,a+b
    print('{},{}'.format(a,b))