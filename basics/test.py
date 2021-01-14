
a = [1, 2, 3, 4, 5, 6]
b = iter(a)
for i in (range(8)):
    c = next(b)
    print(c)

generato = (i for i in range(6))

