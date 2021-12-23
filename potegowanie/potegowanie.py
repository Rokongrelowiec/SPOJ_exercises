def potegowanie():
    l = int((input("Ilosc liczb: ")).strip())
    lst = []
    for i in range(l):
        z = (input("Wejscie: ")).strip()
        s = 1
        for e in range(int(z[2])):
            s *= int(z[0])
        s = str(s)
        lst.append(s[-1])
    for w in lst:
        print(w)

potegowanie()