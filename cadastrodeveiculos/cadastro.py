from classes import Veiculo, GerenciadorVeiculos

def main():
    gerenciador = GerenciadorVeiculos()
    while True:
        print("\nMenu:")
        print("1. Cadastrar veículo")
        print("2. Listar veículos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")
            gerenciador.adicionar_veiculo(marca, modelo, ano)
        elif opcao == "2":
            gerenciador.listar_veiculos()
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
