def validar_nome(nome, tamanho_minimo):
    return nome is not None and len(nome.strip()) >= tamanho_minimo

def validar_cpf(cpf):
    if cpf is None:
        return False
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    return len(cpf_limpo) == 11 

def validar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))
    return len(telefone) in (10, 11)

def validar_email(email):
    if email is None:
        return False
    if "@" in email:
        return True

def validar_numeros_positivos(numero):
    return numero > 0

def buscar_contas(contas,numero):
    for conta in contas:
        if conta.getNumero() == numero:
            return conta
    return None


