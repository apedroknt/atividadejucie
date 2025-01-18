# Funções relacionadas ao cadastro de veículos

def cadastrar_veiculo(veiculos, modelo, placa, ano):
    """Função para cadastrar um veículo"""
    veiculo = {"modelo": modelo, "placa": placa, "ano": ano}
    veiculos.append(veiculo)
    print(f"Veículo com placa {placa} cadastrado com sucesso.")

def listar_veiculos(veiculos):
    """Função para listar todos os veículos cadastrados"""
    if veiculos:
        print("\nLista de veículos cadastrados:")
        for veiculo in veiculos:
            print(f"Modelo: {veiculo['modelo']}, Placa: {veiculo['placa']}, Ano: {veiculo['ano']}")
    else:
        print("Não há veículos cadastrados.")
