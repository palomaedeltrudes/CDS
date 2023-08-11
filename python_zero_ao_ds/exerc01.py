numero = int(input("Digite um numero: "))

if numero <= 5:
    calculate = numero * 10
    print("O valor caculado é: ", calculate)
else:
    if numero >= 6 and numero <= 10:
        calculate = numero * 20
        print("O valor caculado é: ", calculate)
    else:
        if numero >= 11:
            calculate = numero + 100
            print("O valor caculado é: ", calculate)
