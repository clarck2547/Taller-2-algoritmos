from random import randint

def AdivinarDividirVencer(b, e, n):
    numeros = []
    if b == e:
        return b
    for i in range(n):
        guess = randint(b, e)
        numeros.append(guess)
        print("El número", guess, "es Mayor(1), Menor(2) o Igual(0)?")
        inp = int(input())
        if inp == 1:
            e = guess - 1
        elif inp == 2:
            b = guess + 1
        elif inp == 0:
            return guess
    return AdivinarDividirVencer(b, e, n)

def adivinarNumero():
    while True:
        print("Dame el rango superior")
        e = int(input())
        print("Dame la cantidad de numeros a adivinar")
        n = int(input())
        if e >= 0 and n >= 0:   
            print("Piensa un número del 0 al", e)
            print(AdivinarDividirVencer(0, e, n), "es tu número!")
            break

adivinarNumero()
