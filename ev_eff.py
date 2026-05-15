# # Recebe três valores: distância percorrida (km), ???, preço do litro (R$).
# Calcule pelo menos duas das métricas abaixo:
# Custo total;
# Custo por km;
# Exiba cada métrica calculada em uma linha separada.
# Liberdade: você decide a ordem dos cálculos, quais variáveis intermediárias
# Criar e quais métricas priorizar na saída.


dist = float(input("Distância do trajeto (km): "))
consumo_mj_km = float(input("Consumo do veículo (MK/Km): "))
preco_kwh = float(input("Preço do kWh (R$): "))

consumo_kwh_km = consumo_mj_km / 3.6 #fator de conversão de MJ para kWh

energia_total = dist*consumo_kwh_km
custo_total = energia_total * preco_kwh
custo_km = custo_total/dist

print(f"Energia usada: {energia_total:.2f}")
print(f"Custo do trajeto: R$ {custo_total:.2f}")
print(f"Custo por km: R$ {custo_km:.2f}")





