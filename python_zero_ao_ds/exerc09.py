desconto_base = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
previsao_pedidos = [400, 100, 3600, 4100, 4900, 7600, 9500]
previsao_base = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
dias_semana = [1, 2, 3, 4, 5, 6, 7]

desconto_diario = []
for dia in dias_semana:
    if previsao_pedidos[dia-1] > previsao_base[dia-1]:
        desconto_final = desconto_base[dia-1] + ((previsao_pedidos[dia-1] - previsao_base[dia-1])/100)/100
        desconto_diario.append(desconto_final)
    else:
        desconto_final = desconto_base[dia-1]
        desconto_diario.append(desconto_final)

print("O desconto diário é: ")
print(desconto_diario)

