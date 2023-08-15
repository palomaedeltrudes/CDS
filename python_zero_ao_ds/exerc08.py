#Valores dos elementos
n1 = int(53)
n2 = int(9)
n3 = int(54)
n4 = int(91)
n5 = int(84)
n6 = int(54)
n7 = int(7)
n8 = int(51)
n9 = int(60)
n10 = int(86)

#Quantida de elementos
nQtd = int(10)

#Calculando a media dos 10 numeros
media = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10)/nQtd
print("A media é: %.2f"%media)

#Calculando o quadrado da diferença entre os elementos do conjunto e a média
qd1 = (n1-media)**2

qd2 = (n2-media)**2

qd3 = (n3-media)**2

qd4 = (n4-media)**2

qd5 = (n5-media)**2

qd6 = (n6-media)**2

qd7 = (n7-media)**2

qd8 = (n8-media)**2

qd9 = (n9-media)**2

qd10 = (n10-media)**2

#Calculando a média entre os valores encontrados. Essa média é conhecida como variância do conjunto, representada por V.
V = (qd1 + qd2 + qd3 + qd4 + qd5 + qd6 + qd7 + qd8 + qd9 + qd10)/nQtd
print("A variância do conjunto é: %.2f"%V)

#Por fim, o desvio-padrão é a raiz quadrada da variância, ou seja:
desvioPadrao = V ** 0.5
print("O desvio padrao é: %.2f"%desvioPadrao)




