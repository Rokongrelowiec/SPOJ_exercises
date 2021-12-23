def potega():
    z = input("Wejscie: ").split()
    s = 1
    z = [int(x) for x in z]
    for i in range(z[1]):
        s *= z[0]
    print(s)

potega()