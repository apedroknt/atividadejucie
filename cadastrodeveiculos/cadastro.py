# Importando as classes do arquivo 'funcoes.py'
from classes import Veiculo, CadastroVeiculos

def menu():
    """Função para exibir o menu de opções"""
    print("\n--- Cadastro de Veículos ---")
    print("1. Cadastrar veículo")
    print("2. Listar veículos cadastrados")
    print("3. Sair")

def main():
    cadastro = CadastroVeiculos()  # Criando uma instância de CadastroVeiculos

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            placa = input("Digite a placa do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")

            cadastro.cadastrar_veiculo(placa, modelo, ano)

        elif opcao == '2':
            cadastro.listar_veiculos()

        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
