número = int(input("Digite um número para ver a tabuada: "))

print(f"-- Tabuada do {numero} --")

# Laço de repetição para calcular e mostrar a tabuada
for i in range(1, 11):
    # Cálculo do resultado da multiplicação
    resultado = numero * i
    # Exibição do resultado formatado
    print(f"{numero} x {i} = {resultado}")     ...