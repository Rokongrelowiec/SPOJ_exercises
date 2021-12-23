def zabawne_dodawanie_piotrusia():
    lst =[]
    l = int(input('Liczba testów: '))
    for i in range(l):

        z = (input('Wiersz: ')).strip()

        if len(z) < 2:
            # print(z, 0)
            lst.append(int(z))
            lst.append(0)
            lst.append(None)


        else:
            p = 0
            while True:

                if len(z)%2 == 0:
                    z_p = z[:int(len(z)/2)]
                    z_l = z[int((len(z)/2)):]
                    if str(z_p) == str(z_l):
                        break
                    else:
                        p += 1
                        z = int(z) + int(z[::-1])
                        z = str(z)

                else:
                    z_p = z[:int(len(z)/2)]
                    z_l = z[int((len(z)/2)+1):]
                    if str(z_p) == str(z_l):
                        break
                    else:
                        p += 1
                        z = int(z) + int(z[::-1])
                        z = str(z)

            # print(z, p)
            lst.append(int(z))
            lst.append(p)
            lst.append(None)

    for i in lst:
        if i == None:
            print(' ')
        else:
            print(i, end=' ')
            
zabawne_dodawanie_piotrusia()
