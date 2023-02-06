n = int(input("Enter number: "))

x1, x2 = 1, 1
a = x1 * x2
while a < n:
    a //= x1
    x1, x2 = x2, x1 + x2
    a *= x2

if a == n:
    print("Nuber is product")
else:
    print("Number isn't product")
