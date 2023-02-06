n = int(input("Please enter number to find integer square root: "))

i = 0
k = 0
while k <= n:
    k += (1 + i * 2)
    i += 1
print(i - 1)
