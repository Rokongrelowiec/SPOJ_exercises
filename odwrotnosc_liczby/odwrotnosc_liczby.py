def odwrotnosc_liczby():
    w = int(input("Testy: ").strip())
    lst = []
    for e in range(w):
        z = input(f"Wejscie {e+1}: ").split()
        z = [int(x) for x in z]
        i = 2
        while True:
            if (z[1]*i) % z[0] == 1:
                break
            else:
                i += 1
        lst.append(i)

    for q in lst:
        print(q)

odwrotnosc_liczby()