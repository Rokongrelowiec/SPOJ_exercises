def sumy_wielokrotne():
    lst = []
    while True:
        a = input("Wejscie: ").split()
        a = [int(x) for x in a]

        if a[0] == 0 and len(a) == 1:
            lst.append(a[0])
            res = 0
            for i in lst:
                res += i
            lst.append(res)
            break

        else:
            sum = 0
            for i in a:
                sum += i
            lst.append(sum)

    for i in lst:
        print(i)

sumy_wielokrotne()