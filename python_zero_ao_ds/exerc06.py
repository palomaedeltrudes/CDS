numero1 = input("Digite o numero 1: ")
numero2 = input("Digite o numero 2: ")
numero3 = input("Digite o numero 3: ")

if numero1 > numero2:
    if numero1 > numero3:
        print("O maior valor é: ", numero1)
else:
    if numero2 > numero3:        
        print("O maior valor é: ", numero2)
    else:
        print("O maior valor é: ", numero3)
if numero1 < numero2:
    print("O menor valor é: ", numero1)
else:
    if numero2 < numero3:        
        print("O menor valor é: ", numero2)
    else:
        print("O menor valor é: ", numero3)
        