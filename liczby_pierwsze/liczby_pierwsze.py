def liczby_pierwsze():
    l = int((input("Ilosc liczb: ")).strip())
    lst = []
    for i in range(l):
        z = int((input("Podaj liczbe: ")).strip())
        if z < 2:
            lst.append('NIE')
        else: 
            for e in range(2, z):
                if z%e == 0:
                    lst.append('NIE')
                    break
            else:
                lst.append('TAK')
    for i in lst:
        print(i)

liczby_pierwsze()