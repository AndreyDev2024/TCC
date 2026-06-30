from database.conexao import conectar


def registrar_historico_demanda(
    demanda_id,
    usuario_tipo,
    usuario_id,
    acao,
    descricao
):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO historico_demandas
        (demanda_id, usuario_tipo, usuario_id, acao, descricao)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (demanda_id, usuario_tipo, usuario_id, acao, descricao)
    )
    conexao.commit()
    conexao.close()


def listar_historico_por_demanda(demanda_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT * FROM historico_demandas
        WHERE demanda_id = %s
        ORDER BY data_historico DESC
        """,
        (demanda_id,)
    )
    historico = cursor.fetchall()
    conexao.close()
    return historico
