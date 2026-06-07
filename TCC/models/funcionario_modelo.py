from database.conexao import conectar

def cadastrar_funcionario(
    nome,
    cpf,
    email,
    senha,
    tipo,
    setor,
    empresa_id
):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO funcionarios
        (nome_funcionario, cpf_funcionario, email_funcionario, senha_funcionario, tipo_funcionario, setor_funcionario, empresa_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (nome, cpf, email, senha, tipo, setor, empresa_id)
    )

    conexao.commit()
    conexao.close()
def buscar_funcionario_por_cpf(cpf):
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT * FROM funcionarios WHERE cpf_funcionario = %s",
        (cpf,)
    )
    funcionario = cursor.fetchone()
    conexao.close()
    return funcionario
def buscar_funcionario_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        'SELECT * FROM funcionarios WHERE email_funcionario = %s',
        (email,)
    )
    funcionario = cursor.fetchone()
    conexao.close()
    return funcionario