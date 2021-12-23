def kalkulator():
    #own interpretation
    z = input("Wejście: ").split()
    if z[0] == '+':
        print(int(z[1]) + int(z[2]))
    elif z[0] == '-':
        print(int(z[1]) - int(z[2]))
    elif z[0] == '*':
        print(int(z[1]) * int(z[2]))
    elif z[0] == '/':
        print(int(z[1]) // int(z[2]))
    elif z[0] == '%':
        print(int(z[1]) % int(z[2]))

kalkulator()