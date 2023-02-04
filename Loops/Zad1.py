x1=1
x2=1
for i in range(1000000):
    print(x1)
    x1,x2=x2,x2+x1
print(x1)