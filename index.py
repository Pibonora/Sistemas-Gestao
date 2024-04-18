opcoes = ["Cadastrar paciente", "Listar fila de pacientes em espera",
          "Atender paciente", "Listar pacientes atendidos", "Sair"]

# Lista para armazenar os pacientes
pacientes_espera = []
pacientes_atendidos = []

while True:
    print("\nSelecione uma opção:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

    # Solicitar entrada do usuário
    escolha = int(input("Digite o número da opção desejada: "))

    # Verificar a escolha do usuário
    if escolha == 1:
        print("Opção selecionada: Cadastrar paciente")

        # Loop para registrar informações de vários pacientes
        while True:
            nome = input("Digite o nome do paciente: ")
            idade = int(input("Digite a idade do paciente: "))
            queixa = input("Qual a queixa do paciente? ")
            dor = int(input("Em uma escala de 0 a 10, qual é a dor do paciente? "))
            doencas = input("O paciente tem alguma doença? ")
            respiracao = input("O paciente sente falta de ar? ")
            urgencia = input("Qual a emergencia?:\n 1) Emergência:\n 2) Urgência:\n 3) Pouca Urgência:\n 4) Não Urgente ")

            # Adicionar informações do paciente à lista de pacientes em espera
            paciente = {"nome": nome, "idade": idade, "queixa": queixa, "dor": dor,
                        "doencas": doencas, "respiracao": respiracao, "urgencia": urgencia}
            pacientes_espera.append(paciente)
            print("Paciente registrado:", paciente)

            continuar = input("Deseja cadastrar outro paciente? (s/n): ")
            if continuar.lower() != 's':
                break

    elif escolha == 2:
        print("Opção selecionada: Listar fila de pacientes em espera")
        print("Pacientes em espera:")
        
        # Ordenar a lista de pacientes por urgência (emergência primeiro)
        pacientes_espera_ordenados = sorted(pacientes_espera, key=lambda x: x["urgencia"])
        
        # Exibir os pacientes em espera 
        for paciente in pacientes_espera_ordenados:
            print(paciente)


    elif escolha == 3:
        print("Opção selecionada: Atender paciente")
        if len(pacientes_espera) > 0:
                # Ordenar a lista de pacientes por urgência (emergência primeiro)
                pacientes_espera.sort(key=lambda x: x["urgencia"])
                
                # Atender o primeiro paciente da lista 
                paciente_atendido = pacientes_espera.pop(0)
                pacientes_atendidos.append((paciente_atendido["urgencia"], paciente_atendido))
                print("Paciente atendido:", paciente_atendido)
        else:
                print("Não há pacientes na fila de espera.")


    elif escolha == 4:
        print("Opção selecionada: Listar pacientes atendidos")
        print("Pacientes atendidos:")
        
        # Ordenar a lista de pacientes atendidos por urgência (emergência primeiro)
        pacientes_atendidos.sort(key=lambda x: x[0])
        
        # Exibir os pacientes atendidos
        for _, paciente in pacientes_atendidos:
            print(paciente)


    elif escolha == len(opcoes):
        print("Opção selecionada: Sair")
        break

    else:
        print("Opção inválida!")