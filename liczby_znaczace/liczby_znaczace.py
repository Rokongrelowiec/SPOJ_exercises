def liczby_znaczące():
    w = int(input("Testy: ").strip())
    lst = []
    for e in range(w):
        z = input("Wejscie: ").split()
        z = [int(x) for x in z]
        lst_res = []
        lst_dzielnikow = []
        sum = 0
        avg = 0
        for s in range(z[0], z[1]+1):
            for g in range(2, s):
                if s%g == 0:
                    lst_dzielnikow.append(g)
            for r in range(len(lst_dzielnikow)):
                sum += lst_dzielnikow[r]
            if len(lst_dzielnikow) > 0:
                avg = sum/len(lst_dzielnikow)
                if avg <= s**0.5:
                    lst_res.append(s)
        l = 0
        for g in lst_res:
            l += 1
        lst.append(l)
        
    for i in lst:
        print(i)

liczby_znaczące()