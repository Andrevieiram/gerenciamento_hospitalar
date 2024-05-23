from Funcoes import *



print("╔══════════════════════════════════╗")
print("║     Sistema de Gerenciamento     ║")
print("║          Hospitalar              ║")
print("╚══════════════════════════════════╝")

menu = True
while menu:

    print("╔══════════════════════════════════╗")
    print("║              Menu                ║")
    print("║  1) Cadastrar Paciente           ║")
    print("║  2) Pesquisar Paciente           ║")
    print("║  3) Cadastrar Médico             ║")
    print("║  4) Pesquisar Médico             ║")
    print("║  5) Excluir Paciente             ║")
    print("║  6) Excluir Médico               ║")
    print("║  7) Sair                         ║")
    print("╚══════════════════════════════════╝\n")


    opcao = int(input('Escolha uma opção: '))


    if opcao == 1:
        cpf = input("Cpf: ")
        nome = input("Nome: ")
        idade = (input("Idade: "))
        rua = input("Endereço (rua): ")
        numero = input("Endereço (Número): ")
        bairro = input("Endereço (Bairro): ")
        telefone = input("Telefone: ")

        endereco = rua,numero,bairro

        if cpf and nome and idade and rua and numero and bairro and telefone and endereco:
            paciente = novo_paciente(cpf, nome, idade, endereco, telefone)    
        else:
            print("Por favor preencha todos os campos obrigatorios.\n")

    elif opcao == 2:
        cpf = input("Digite o CPF do paciente: ")

        paciente = pesquisar_paciente(cpf)

        if paciente:
            mostra_paciente(paciente)  
        else:
            print("Paciente não encontrado.\n")

    elif opcao == 3:
        crm = input('Crm: ')
        nome = input('Nome: ')
        especialidade = input('Especialidade: ')
        telefone = input('Telefone: ')

        if crm and nome and especialidade and telefone:
            medico = novo_medico(crm, nome, especialidade, telefone)          
        else :
            print("Por favor, preencha todos os campos obrigatorios.\n")

    elif opcao == 4:
        crm = input("Digite o CRM do médico: ")

        medico = pesquisar_medico(crm)

        if medico:
            mostra_medico(medico)
        else:
            print("Médico não encontrado.\n")

    elif opcao == 5:
        cpf = input("Digite o CPF do paciente a ser removido: ")

        if remover_paciente(cpf):
            print("Paciente removido com sucesso!\n")
        else:
            print("Paciente não encontrado.\n")

    elif opcao == 6:
        crm = input("Digite o CRM do médico a ser removido: ")

        if remover_medico(crm):
            print("Médico removido com sucesso!\n")
        else:
            print("Médico não encontrado.\n")

    elif opcao == 7:
        print("Sistema finalizado")

        menu = False
    else:
        print('Digite uma opção do menu válida!\n')
