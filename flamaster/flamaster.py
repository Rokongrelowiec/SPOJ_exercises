
def flamaster():
    l = (input("Ilosc linii: ")).strip()
    lst = []
    for i in range(int(l)):
        z = input('Zdanie: ')
        dct = {}
        w = ""
        for e in z:
            if e in dct:
                dct[e] += 1
            else:
                dct[e] = 1
        for q in dct:
            if dct[q] > 2:
                w += q + str(dct[q])
            else:
                for i in range(dct[q]):
                    w += q
        lst.append(w)
    for s in lst:
        print(s)

flamaster()