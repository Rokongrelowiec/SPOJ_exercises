def podzielnosc():
    l = (input("Testy: ")).strip()
    lst = []
    for i in range(int(l)):
        z = input("Wejscie: ")
        z = z.split()
        z = [int(i) for i in z]
        for i in range(z[1], z[0]):
            if i%z[1] == 0 and i%z[2] != 0:
                lst.append(i)
        lst.append(None)
    for w in lst:
        if w == None:
            print()
        else:
            print(w, end=' ')
    print()

podzielnosc()
