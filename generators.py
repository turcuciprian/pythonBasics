def fib(nr):
    a,b = 0,1
    for i in range(0,nr):
        yield '{},{}'.format(i+1,a)
        a, b = b, a + b

for item in fib(10):
    print(item)

print('\n\n\n')

