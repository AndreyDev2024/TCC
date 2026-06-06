from database.conexao import conectar

def cadastrar_empresa(
    nome,
    cnpj,
    email,
    senha,
    nicho
):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        '''
        INSERT INTO empresas
        (nome_empresa, cnpj_empresa, email_empresa, senha_empresa, nicho_empresa)
        VALUES(%s, %s, %s, %s, %s)
        ''',
        (nome, cnpj, email, senha, nicho)
    )
    conexao.commit()
    conexao.close()
    
def buscar_empresa_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        'SELECT * FROM empresas WHERE email_empresa = %s',
        (email,)
    )
    empresa = cursor.fetchone()
    conexao.close()
    return empresa

def buscar_empresa_por_cnpj(cnpj):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        'SELECT * FROM empresas WHERE cnpj_empresa = %s',
        (cnpj,)
    )
    empresa = cursor.fetchone()
    conexao.close()
    return empresa