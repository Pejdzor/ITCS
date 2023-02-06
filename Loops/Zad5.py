n = int(input("Please enter number to find it's square root: "))

a = 1
b = n

while abs(a - b) > 1e-8:
    a, b = (a + b) / 2, n / a
print(a)
