import datetime
year = datetime.datetime.today().year

im, jm = 1, year
for i in range(1, year):
    for j in range(i, year):
        x1, x2 = i, j
        while x1 < year:
            x1, x2 = x2, x1 + x2
        if x1 == year and i + j < im + jm:
            im, jm = i, j
print(im, jm)