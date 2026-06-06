def validar_cpf(cpf):
    cpf = str(cpf)
    if not cpf.isdigit():
        return 'CPF invalido, tente novamente!'
    if len(cpf) != 11:
        return 'CPF incorreto, tente novamnte!'
    return True
def validar_cnpj(cnpj):
    cnpj = str(cnpj)
    if not cnpj.isdigit():
        return 'CNPJ invalido, tente novamente!'
    if len(cnpj) != 14:
        return 'CNPJ incorreto, tente novamnte!'
    return True
def validar_email(email):
    if '@' not in email:
        return 'Email invalido, tente novamente!'
    if "." not in email:
        return 'Dominio invalido, tente novamente!'
    return True
def validar_senha(senha):
    if len(senha) < 8:
        return "Senha curta, tente novamente!"
    if not any(
        letra.isupper()
        for letra in senha
    ):
        return 'Sua senha Precisa conter uma letra maiuscula!'
    if not any(
        letra.islower()
        for letra in senha
    ):
        return 'Sua senha Precisa conter uma letra minuscula!'
    if not any(
        letra.isdigit()
        for letra in senha
    ):
        return 'Sua senha Precisa conter um numero'
    if not any(
        especial in "!@#$%&?"
        for especial in senha
    ):
        return 'Sua senha Precisa conter um caractere especial!'
    return True