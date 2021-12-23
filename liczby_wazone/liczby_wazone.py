
def liczby_wywazone():
    w = int(input("Testy: ").strip())
    lst = []
    for e in range(w):
        lst_p = []
        lst_n = []
        z = int(input(f"Wejscie {e+1}: ").strip())
        z += 1

        for q in range(1, z+1):
            if z % q == 0:
                if q % 2 == 0:
                    lst_p.append(q)
                else:
                    lst_n.append(q)
        
        while True:
            if len(lst_p) == len(lst_n):
                break
            else:
                z += 1
                lst_p = []
                lst_n = []
                for q in range(1, z+1):
                    if z % q == 0:
                        if q % 2 == 0:
                            lst_p.append(q)
                        else:
                            lst_n.append(q)

        lst.append(z)
    for i in lst:
        print(i)

liczby_wywazone()