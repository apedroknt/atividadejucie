class Veiculo:
    def __new__(cls, *args, **kwargs):
        print("Criando um novo veículo...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
    

class GerenciadorVeiculos:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, marca, modelo, ano):
        veiculo = Veiculo(marca, modelo, ano)
        self.veiculos.append(veiculo)

    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("Veículos cadastrados:")
            for idx, veiculo in enumerate(self.veiculos, 1):
                print(f"{idx}. {veiculo}")
    
