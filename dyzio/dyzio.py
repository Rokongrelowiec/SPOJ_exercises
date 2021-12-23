def dyzio():
    l = (input("Testy: ")).strip()
    lst = []
    for i in range(int(l)):
        z = input("Przedział: ").split()
        z = [int(x) for x in z]
        v = 0
        for e in range(z[0], z[1]+1):
            for w in range(2, e):
                if e % w == 0:
                    break
            else:
                v += 1
        lst.append(v)

    for i in lst:
        print(i)

dyzio()