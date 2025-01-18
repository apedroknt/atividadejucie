from classes import Veiculo, Frota, Motorista


def obter_inteiro(mensagem, minimo=1, maximo=None):
    """
    Solicita ao usuário um número inteiro, validando a entrada.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo or (maximo is not None and valor > maximo):
                raise ValueError
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número válido.")


def main():
    frota = Frota()
    motoristas = []

    while True:
        print("\nMenu:")
        print("1. Cadastrar veículo na frota")
        print("2. Listar veículos da frota")
        print("3. Cadastrar motorista")
        print("4. Associar motorista a veículo")
        print("5. Listar motoristas de um veículo")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")
            veiculo = Veiculo(marca, modelo, ano)
            frota.adicionar_veiculo(veiculo)
            print("Veículo cadastrado com sucesso!")
        elif opcao == "2":
            print("\nVeículos cadastrados na frota:")
            print(frota.listar_veiculos())
        elif opcao == "3":
            nome = input("Digite o nome do motorista: ")
            idade = input("Digite a idade do motorista: ")
            motorista = Motorista(nome, idade)
            motoristas.append(motorista)
            print("Motorista cadastrado com sucesso!")
        elif opcao == "4":
            if not frota.veiculos:
                print("\nNenhum veículo cadastrado na frota.")
                continue

            if not motoristas:
                print("\nNenhum motorista cadastrado.")
                continue

            print("\nVeículos cadastrados:")
            print(frota.listar_veiculos())
            veiculo_idx = obter_inteiro("Escolha o número do veículo: ", 1, len(frota.veiculos)) - 1

            print("\nMotoristas disponíveis:")
            for idx, motorista in enumerate(motoristas, 1):
                print(f"{idx}. {motorista}")
            motorista_idx = obter_inteiro("Escolha o número do motorista: ", 1, len(motoristas)) - 1

            veiculo_selecionado = frota.veiculos[veiculo_idx]
            motorista_selecionado = motoristas[motorista_idx]
            veiculo_selecionado.adicionar_motorista(motorista_selecionado)
            print(f"\n{motorista_selecionado} foi associado ao veículo {veiculo_selecionado}.")
        elif opcao == "5":
            if not frota.veiculos:
                print("\nNenhum veículo cadastrado na frota.")
                continue

            print("\nVeículos cadastrados:")
            print(frota.listar_veiculos())
            veiculo_idx = obter_inteiro("Escolha o número do veículo: ", 1, len(frota.veiculos)) - 1

            veiculo_selecionado = frota.veiculos[veiculo_idx]
            motoristas_relacionados = veiculo_selecionado.listar_motoristas()

            if "Nenhum motorista" in motoristas_relacionados:
                print(f"\nO veículo {veiculo_selecionado} não está sendo dirigido por nenhum motorista.")
            else:
                print(f"\nO veículo {veiculo_selecionado} está sendo dirigido por:")
                print(motoristas_relacionados)
        elif opcao == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
