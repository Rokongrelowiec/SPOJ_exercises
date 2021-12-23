def not_so_fast_multiplication():
    w = int(input("Testy: ").strip())
    lst = []
    for e in range(w):
        z = input("Wejście: ").split()
        z = [int(x) for x in z]
        s = z[0]*z[1]
        lst.append(s)
    for i in lst:
        print(i)

not_so_fast_multiplication()