numero1 = input()
numero2 = input()
numero3 = input()

if numero1 > numero2 and numero1 > numero3:
    print("O maior valor é: ", numero1)
else:
    print("O maior valor é: ", numero3)

    if numero2 > numero3:        
        print("O maior valor é: ", numero2)
    else:
        print("O maior valor é: ", numero3)
