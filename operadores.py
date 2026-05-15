# Operadores lógicos:
nota = float(input("Nota (0-10): "))
freq = float(input("Frequência(%): "))

if nota >= 7 and freq >= 75: # and: operação lógica "E", só é verdade se ambos forem verdade"
    situacao = "Aprovado"
elif nota < 6 or freq < 70:
    situacao = "Reprovado sem recuperação"
else:
    situacao = "Recuperação"
    
# or: operação lógica "OU", é verdade se qualquer um for verdade
# Complete o exercício mostrando "recuperação" ou "reprovado"
# Condição para reprovação sem recuperação: nota menor que 6 ou frequência menor que 70% 

print(f"Situação do estudante: {situacao}")