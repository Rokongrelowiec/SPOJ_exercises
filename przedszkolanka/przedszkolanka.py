def przedszkolanka():
    l = input("Liczba linii: ")
    l = l.strip()
    lst = []
    for i in range(int(l)):
        z = input("Liczba cukierkow: ")
        z = z.split()
        c = [int(i) for i in z]
        c0 = c[0]
        c1 = c[1]
        while True:
            if c[0] == c[1]:
                break
            elif c[0] > c[1]:
                c[1] += c1
            else:
                c[0] += c0


        lst.append(c[0])
    for w in lst:
        print(w)

przedszkolanka()