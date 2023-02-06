a = 0
b = 10
x = (a + b) / 2
y = x ** x
while abs(y - 2020) > 1e-8:
    if y - 2020 < 0:
        a = x
        x = (a + b) / 2
        y = x ** x
    elif y - 2020 > 0:
        b = x
        x = (a + b) / 2
        y = x ** x
print(x)