# Criação da classe pai
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Criação da classe filha que herda da classe pai
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

# Criação de objetos para teste
veiculo1 = Veiculo("Toyota", "Corolla")
carro1 = Carro("Honda", "Civic", 4)

# Exibição dos atributos dos objetos
print("\n--- Informações do Veículo ---")
print(f"Marca: {veiculo1.marca}")
print(f"Modelo: {veiculo1.modelo}" )

print("\n--- Informações do Carro ---")
print(f"Marca: {carro1.marca}")
print(f"Modelo {carro1.modelo}:")
print(f"Portas {carro1.portas}:")