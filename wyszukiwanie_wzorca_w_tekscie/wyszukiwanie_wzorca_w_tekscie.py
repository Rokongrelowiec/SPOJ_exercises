def wyszukiwanie_wzorca_w_tekscie():
    w = int(input("Testy: ").strip())
    lst = []
    for e in range(w):
        lst_input = []
        for r in range(3):
            var = input(f"{r+1} line: ").strip()
            lst_input.append(var)

        if len(lst_input[1]) > len(lst_input[2]):
            continue
        else:
            for i in range(len(lst_input[2])):
                var = lst_input[2][i:i+len(lst_input[1])]
                if var == lst_input[1]:
                    lst.append(i)

    for i in lst:
        print(i)

            
wyszukiwanie_wzorca_w_tekscie()