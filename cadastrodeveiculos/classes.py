# Classe que representa um veículo
class Veiculo:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Placa: {self.placa}, Modelo: {self.modelo}, Ano: {self.ano}"

# Classe para gerenciar o cadastro de veículos
class CadastroVeiculos:
    def __init__(self):
        self.veiculos = []

    def cadastrar_veiculo(self, placa, modelo, ano):
        """Cadastra um veículo"""
        veiculo = Veiculo(placa, modelo, ano)
        self.veiculos.append(veiculo)
        print(f"Veículo com placa {placa} cadastrado com sucesso.")

    def listar_veiculos(self):
        """Lista todos os veículos cadastrados"""
        if self.veiculos:
            print("\nLista de veículos cadastrados:")
            for veiculo in self.veiculos:
                print(veiculo)
        else:
            print("Não há veículos cadastrados.")
