# Usa Divisão interia e Resto (módulo):

valor1 = 7
valor2 = 3

div = valor1 / valor2
divint = valor1 // valor2
mod = valor1 % valor2

print(f"Divisão: {valor1}/{valor2}={div}")
print(f"Divisão inteira: {valor1} // {valor2}={divint} ")
print(f"Resto da Divisão inteira: {valor1} % {valor2}={mod} ")

# Receba um número de segundos do usuário
# Calcule horas, minutos e segundos usando // e %
# Exiba no formato HH:MM:SS, use var:02d para formato.

#print(f"Resultado: {horas:02d}")

#segundos_str = input("Digite tempo em segundos: ")
#segundos = int(segundos_str)

entrada_segundos = int(input("Digite tempo em segundos: "))
print(f"Segundos digitado: {segundos}")
horas = entrada_segundos // 3600
segundos_restantes = entrada_segundos % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"Resultado em horas {horas:02d}:{minutos:02d}:{segundos:02d}")

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
