def dzielniki_liczb():
    w = input("Testy: ").strip()
    lst = []
    for e in range(int(w)):
        z = input("Wejście: ").split()
        z = [int(x) for x in z]
        if z[0] % z[1] == 0:
            lst.append("TAK")
        else:
            lst.append("NIE")

    for i in lst:
        print(i)
    
dzielniki_liczb()