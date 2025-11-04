número = int(input("Digite um número para ver a tabuada: "))

print(f"---Tabuada do {número}---")
for i in range(1,11):
    print(f"{número} x {i} = {número * i}")