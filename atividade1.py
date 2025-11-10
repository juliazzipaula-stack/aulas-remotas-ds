# Pergunta o nome e guarda na variável 'nome'
nome = input("Qual é o seu nome? ")

# Pergunta a idade e guarda na variável 'idade_texto'
idade_texto = input("Qual a sua idade? ")

# Converte a idade de texto para inteiro e guarda na variável 'idade'
idade = int(idade_texto)

# Cria a lógica condicional para verificar se a idade é maior ou igual a 18
if idade >= 18:
    # Mensagem para usuário maior de idade
    print(f"Olá {nome}, você é maior de idade.")
else:
    # Mensagem para usuário menor de idade
    print(f"Olá {nome}, você é menor de idade.")