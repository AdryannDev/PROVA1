y = 1
z = []
for x in range(3):
    w = int(input(f"coloque o numero {y}: "))
    z.append(w)
    y = y + 1

z.sort()
y = 2
for x in range(3):
    print(z[y])
    y = y - 1