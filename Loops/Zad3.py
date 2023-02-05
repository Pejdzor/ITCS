fsum = int(input("Please enter positive sum to find: "))
fib = []

x1, x2 = 1, 1
while x1 <= fsum:
    fib.append(x1)
    x1, x2 = x2, x1 + x2
p, q = 0, 0
csum = 0
while p <= q and q < len(fib):
    print(p, q, csum)
    if csum == fsum:
        print("Subsequence exists")
        break
    if csum < fsum:
        csum += fib[q]
        q += 1
    if csum > fsum:
        csum -= fib[p]
        p += 1
else:
    print("Subsequence doesn't exist")
