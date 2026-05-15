# Calculadora de IMC:
# Solicita peso e altura, entrega IMC (numérico)

#input: imprime texto, coleta um dado e o armazena na variável:
peso_str = input("Peso (kg): ")

#float: converte texto (string) para número com vírgula:
peso = float(peso_str)


print(f"Peso digitado: {peso}")

#complete o programa para calcular o IMC

#altura = float(input("Digite sua altura: "))
altura_str = input("Digite sua altura em metros(m): ")
altura = float(altura_str)
print(f"Altura digitada: {altura:.2f}")

#altura_quadrado = altura * altura
#imc = peso / altura_quadrado       

# Fórmula: peso / (altura **2) # parêntese opcional nesse caso, para legibilidade.

imc = peso / altura **2

#imc = peso / altura_quadrado

print(f"Seu IMC é {imc:.2f}")

if imc < 18.5: #SE
    categoria = "Abaixo do peso"
elif imc < 25: # "Senão se", abreviação de else if
     categoria = "Normal"
elif imc < 29.9: # 25 - 29,9 Sobrepeso
     categoria = "Sobrepeso"
elif imc < 34.9: # 30 - 34,9 Obesidade grau I
     categoria = "Obesidade grau I" 
elif imc < 39.9: # 35 - 39,9 Obesidade grau II
     categoria = "Obesidade grau II"
else:
     categoria = "Obeso"
#elif imc >= 40: # Obesidade Mórbida
     #categoria = "Obesidade Mórbida"
print(f"Categoria: {categoria}")
# adicione categorias faltantes: acima do peso, obeso, etc.
# como fazer um senão sem se?