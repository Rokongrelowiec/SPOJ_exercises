def string_merge():
    l = (input("Testy: ")).strip()
    lst = []
    for i in range(int(l)):
        res = ''
        w = (input('Wyraz: '))
        w = w.split()
        min = 0

        if len(w[0]) > len(w[1]):
            min = len(w[1])
        else:
            min = len(w[0])

        for e in range(min):
            res = res + w[0][e]
            res = res + w[1][e]
        lst.append(res)
    
    for q in lst:
        print(q)

string_merge()