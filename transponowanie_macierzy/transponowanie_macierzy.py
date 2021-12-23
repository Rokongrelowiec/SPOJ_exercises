def transponowanie_macierzy():
    z = input("Wymiary: ").split()
    z = [int(i) for i in z]
    lst = []
    for i in range(z[0]):
        a = input("Liczby: ").split()
        for e in a:
            lst.append(e)

    for i in range(z[1]):
        for e in range(i, len(lst), z[1]):
            print(lst[e], end= " ")
        print()
    
transponowanie_macierzy()