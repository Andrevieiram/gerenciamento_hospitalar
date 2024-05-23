listaPacientes = []
listaMedicos = []

def novo_paciente(cpf, nome, idade, endereco, telefone):
    for paciente in listaPacientes:
        if paciente['Cpf'] == cpf:
            print("O paciente ja possui cadastro!")

            return False
    else:
            
        paciente = {
            'Cpf': cpf,
            'Nome': nome,
            'Idade': idade,
            'Endereço': endereco,
            'Telefone': telefone}
        
    listaPacientes.append(paciente)

    print("Cadastro feito com sucesso.")
    
    return paciente

def novo_medico(crm, nome, especialidade, telefone):
    for medico in listaMedicos:
        if medico['Crm'] == crm:
            print('Medico ja possui cadastro!')

            return False
    else:
        medico = {
            'Crm': crm,
            'Nome': nome,
            'Especialidade': especialidade,
            'Telefone': telefone}
        listaMedicos.append(medico)

        print("Cadastro feito com sucesso.")

        return medico

def remover_paciente(cpf):
    for paciente in listaPacientes:
        if paciente['Cpf'] == cpf:
            listaPacientes.remove(paciente)

            return True
        
    return False

def remover_medico(crm):
    for medico in listaMedicos:
        if medico['Crm'] == crm:
            listaMedicos.remove(medico)

            return True
        
    return False

def pesquisar_paciente(cpf):
    for paciente in listaPacientes:
        if paciente['Cpf'] == cpf:
            

            return paciente
            
        
    return None

def pesquisar_medico(crm):
    for medico in listaMedicos:
        if medico['Crm'] == crm:

            return medico
        
    return None

def mostra_paciente(paciente):
    nome_encontrado = paciente['Nome']
    idade_encontrada = paciente['Idade']
    endereco_encontrado = paciente['Endereço']
    telefone_encontrado = paciente['Telefone']
    cpf_encontrado = paciente['Cpf']

    return print(f' Paciente: ',nome_encontrado,'\n','Idade: ',idade_encontrada,'\n','Endereço: ',endereco_encontrado,'\n','Telefone: ',telefone_encontrado,'\n','CPF: ',cpf_encontrado,'\n')

def mostra_medico(medico):
    nome_encontrado = medico['Nome']
    especialidade_encontrada = medico['Especialidade']
    telefone_encontrado = medico['Telefone']
    crm_encontrado = medico['Crm']

    return print(f' Médico: ',nome_encontrado,'\n','Especialidade: ',especialidade_encontrada,'\n','Telefone: ',telefone_encontrado,'\n','Crm: ',crm_encontrado,'\n')