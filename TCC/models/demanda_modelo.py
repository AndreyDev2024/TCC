from database.conexao import conectar


def cadastrar_demanda(
    titulo,
    descricao,
    status,
    setor,
    cidade,
    empresa_id,
    funcionario_id
):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO demandas
        (
            titulo_demanda,
            descricao_demanda,
            status_demanda,
            setor_demanda,
            cidade_demanda,
            empresa_id,
            funcionario_id
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            titulo,
            descricao,
            status,
            setor,
            cidade,
            empresa_id,
            funcionario_id
        )
    )
    conexao.commit()
    demanda_id = cursor.lastrowid
    conexao.close()
    return demanda_id


def buscar_demanda_por_id(demanda_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT * FROM demandas
        WHERE id_demanda = %s
        """,
        (demanda_id,)
    )
    demanda = cursor.fetchone()
    conexao.close()
    return demanda


def listar_demandas(
    empresa_id,
    setor=None,
    status=None,
    funcionario_id=None,
    cidade=None
):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    filtros = ["empresa_id = %s"]
    valores = [empresa_id]

    if setor:
        filtros.append("setor_demanda = %s")
        valores.append(setor)
    if status:
        filtros.append("status_demanda = %s")
        valores.append(status)
    if funcionario_id:
        filtros.append("funcionario_id = %s")
        valores.append(funcionario_id)
    if cidade:
        filtros.append("cidade_demanda = %s")
        valores.append(cidade)

    cursor.execute(
        f"""
        SELECT * FROM demandas
        WHERE {' AND '.join(filtros)}
        ORDER BY data_criacao DESC
        """,
        tuple(valores)
    )
    demandas = cursor.fetchall()
    conexao.close()
    return demandas


def editar_demanda(demanda_id, campos):
    conexao = conectar()
    cursor = conexao.cursor()
    colunas = []
    valores = []

    for coluna, valor in campos.items():
        colunas.append(f"{coluna} = %s")
        valores.append(valor)

    valores.append(demanda_id)
    cursor.execute(
        f"""
        UPDATE demandas
        SET {', '.join(colunas)}
        WHERE id_demanda = %s
        """,
        tuple(valores)
    )
    conexao.commit()
    conexao.close()


def atualizar_status_demanda(demanda_id, status):
    conexao = conectar()
    cursor = conexao.cursor()
    if status == "concluida":
        cursor.execute(
            """
            UPDATE demandas
            SET status_demanda = %s,
                data_conclusao = CURRENT_TIMESTAMP
            WHERE id_demanda = %s
            """,
            (status, demanda_id)
        )
    else:
        cursor.execute(
            """
            UPDATE demandas
            SET status_demanda = %s,
                data_conclusao = NULL
            WHERE id_demanda = %s
            """,
            (status, demanda_id)
        )
    conexao.commit()
    conexao.close()
