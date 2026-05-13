# comentário iniciam com # e terminam no fim da linha

# variável possuem vários tipos. 
# Variáveis são sensíveis a maiúscula e minúscula na maioria das linguagens
# nomes de variável não podem começar com número, mas podem ter número no meio ou fim.
# Em Python, o tipo(numérico, texto, etc.) não é especificado explicitamente:

preço_original = 150.0      # número sem ponto é ínteiro, com ponto é float (decimal);
percentual_desconto = 20 
moeda = "R$" # variável contendo texto usa aspas (simples ou dupla)

valor_do_desconto = preço_original * (percentual_desconto / 100)
preco_final = preço_original - valor_do_desconto

# Para mostrar o resultado, use a função print()
print("Exemplo de cálculo de desconto: ")
print(f"Entrada: {moeda} {preço_original:.2f}") #como imprimir com 2 zeros após o ponto?
#Escreva 
# "valor de desconto: xx%: R$ XX"
# "Preço final: R$ XX"
print(f"Valor de desconto de {percentual_desconto}%: {moeda} {valor_do_desconto:.2f}")
print(f"Preço final: {moeda} {preco_final:.2f}")

