class Veiculo:
    def __new__(cls, *args, **kwargs):
        print("Criando um novo veículo...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motoristas = []  # Lista de motoristas associados ao veículo

    def adicionar_motorista(self, motorista):
        """Associa um motorista ao veículo."""
        self.motoristas.append(motorista)

    def listar_motoristas(self):
        """Lista os motoristas associados ao veículo."""
        if not self.motoristas:
            return "Nenhum motorista associado a este veículo."
        return "\n".join([str(motorista) for motorista in self.motoristas])

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"


class Frota:
    def __new__(cls, *args, **kwargs):
        print("Criando uma nova frota...")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        """Adiciona um veículo à frota."""
        self.veiculos.append(veiculo)

    def listar_veiculos(self):
        """Lista todos os veículos cadastrados na frota."""
        if not self.veiculos:
            return "Nenhum veículo cadastrado na frota."
        return "\n".join([f"{idx + 1}. {veiculo}" for idx, veiculo in enumerate(self.veiculos)])


class Motorista:
    def __new__(cls, *args, **kwargs):
        print("Criando um novo motorista...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"
