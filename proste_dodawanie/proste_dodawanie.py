def proste_dodawanie():
    
    l = (input("Testy: ")).strip()
    lst = []
    for q in range(int(l)):
       
        s = input("Liczba elementow: ") # mozna zakomentowac ta linie
        # powyzsza linia istnieje tylko na potrzeby zadania!

        z = (input("Liczby: ")).split()
        sum = 0
        z = [int(i) for i in z]
        for i in z:
            sum += i
        lst.append(sum)

    for w in lst:
        print(w)
        
proste_dodawanie()
            