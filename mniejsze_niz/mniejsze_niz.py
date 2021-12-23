def mniejsze_niz():
    lst = []
    z = int(input("Liczba elementow A: ").strip())
    lst_test = []
    for q in range(z):
        w = int(input(f"Element nr {q+1}: ".strip()))
        lst_test.append(w)
    
    print()
    p = int(input("Liczba k: ").strip())
    lst_check = []
    for e in range(p):
        o = int(input(f"Element nr {e+1}: ".strip()))
        lst_check.append(o)


    
    for i in lst_check:
        y = 0 
        for s in lst_test:
            if s < i:
                y += 1
        lst.append(y)
    
    for t in lst:
        print(t)
    
mniejsze_niz()