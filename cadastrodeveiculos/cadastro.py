# Importando as funções do arquivo 'funcoes.py'
from funcoes import cadastrar_veiculo, listar_veiculos

def menu():
    """Função para exibir o menu de opções"""
    print("\n--- Cadastro de Veículos ---")
    print("1. Cadastrar veículo")
    print("2. Listar veículos cadastrados")
    print("3. Sair")

def main():
    veiculos = []  # Lista para armazenar os veículos cadastrados

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            modelo = input("Digite o modelo do veículo: ")
            placa = input("Digite a placa do veículo: ")
            ano = input("Digite o ano do veículo: ")

            cadastrar_veiculo(veiculos, modelo, placa, ano)

        elif opcao == '2':
            listar_veiculos(veiculos)

        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
