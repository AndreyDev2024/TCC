from database.conexao import conectar


def buscar_perfil_empresa(empresa_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT
            id_empresa,
            nome_empresa,
            cnpj_empresa,
            email_empresa,
            nicho_empresa,
            foto_empresa
        FROM empresas
        WHERE id_empresa = %s
        """,
        (empresa_id,)
    )
    empresa = cursor.fetchone()
    conexao.close()
    return empresa


def buscar_perfil_funcionario(funcionario_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT
            id_funcionario,
            nome_funcionario,
            cpf_funcionario,
            email_funcionario,
            tipo_funcionario,
            setor_funcionario,
            foto_funcionario,
            empresa_id
        FROM funcionarios
        WHERE id_funcionario = %s
        """,
        (funcionario_id,)
    )
    funcionario = cursor.fetchone()
    conexao.close()
    return funcionario


def buscar_empresa_com_senha(empresa_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT id_empresa, email_empresa, senha_empresa
        FROM empresas
        WHERE id_empresa = %s
        """,
        (empresa_id,)
    )
    empresa = cursor.fetchone()
    conexao.close()
    return empresa


def buscar_funcionario_com_senha(funcionario_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT id_funcionario, email_funcionario, senha_funcionario
        FROM funcionarios
        WHERE id_funcionario = %s
        """,
        (funcionario_id,)
    )
    funcionario = cursor.fetchone()
    conexao.close()
    return funcionario


def buscar_empresa_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT id_empresa
        FROM empresas
        WHERE email_empresa = %s
        """,
        (email,)
    )
    empresa = cursor.fetchone()
    conexao.close()
    return empresa


def buscar_funcionario_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT id_funcionario
        FROM funcionarios
        WHERE email_funcionario = %s
        """,
        (email,)
    )
    funcionario = cursor.fetchone()
    conexao.close()
    return funcionario


def atualizar_empresa(empresa_id, campos):
    conexao = conectar()
    cursor = conexao.cursor()
    colunas = []
    valores = []

    for coluna, valor in campos.items():
        colunas.append(f"{coluna} = %s")
        valores.append(valor)

    valores.append(empresa_id)
    cursor.execute(
        f"""
        UPDATE empresas
        SET {', '.join(colunas)}
        WHERE id_empresa = %s
        """,
        tuple(valores)
    )
    conexao.commit()
    conexao.close()


def atualizar_funcionario(funcionario_id, campos):
    conexao = conectar()
    cursor = conexao.cursor()
    colunas = []
    valores = []

    for coluna, valor in campos.items():
        colunas.append(f"{coluna} = %s")
        valores.append(valor)

    valores.append(funcionario_id)
    cursor.execute(
        f"""
        UPDATE funcionarios
        SET {', '.join(colunas)}
        WHERE id_funcionario = %s
        """,
        tuple(valores)
    )
    conexao.commit()
    conexao.close()
