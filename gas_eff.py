# Instruções próximo exercício:

# Recebe três valores: distância percorrida (km), km/l, preço do litro (R$).
# Calcule pelo menos duas das métricas abaixo:
# Custo total;
# Custo por km;
# Exiba cada métrica calculada em uma linha separada.
# Liberdade: você decide a ordem dos cálculos, quais variáveis intermediárias
# Criar e quais métricas priorizar na saída.


# O que fazer com carro elétrico ?
# Apapte a calculadora.

dist = float(input("Distância do trajeto (km): "))
kml = float(input("Consumo do veículo: "))
custo_l = float(input("Custo do litro de combust´viel (R$/L): "))

litros_necessarios = dist / kml

print(f"Litros usados: {litros_necessarios:.2f}")
custo_total = custo_l * litros_necessarios
print(f"Custo do trajeto: R$ {custo_total:.2f}")
custo_km = custo_total / dist
print(f"Custo por km: R$ {custo_km:.2f}")