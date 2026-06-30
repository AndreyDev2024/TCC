from database.conexao import conectar


def listar_demandas_por_status(empresa_id, status):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT
            d.*,
            f.nome_funcionario
        FROM demandas d
        LEFT JOIN funcionarios f
            ON d.funcionario_id = f.id_funcionario
        WHERE d.empresa_id = %s
            AND d.status_demanda = %s
        ORDER BY d.data_criacao DESC
        """,
        (empresa_id, status)
    )
    demandas = cursor.fetchall()
    conexao.close()
    return demandas


def listar_demandas_pendentes(empresa_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT
            d.*,
            f.nome_funcionario
        FROM demandas d
        LEFT JOIN funcionarios f
            ON d.funcionario_id = f.id_funcionario
        WHERE d.empresa_id = %s
            AND d.status_demanda IN ('aberta', 'em_andamento')
        ORDER BY d.data_criacao DESC
        """,
        (empresa_id,)
    )
    demandas = cursor.fetchall()
    conexao.close()
    return demandas


def contar_funcionarios(empresa_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT COUNT(*) AS quantidade_funcionarios
        FROM funcionarios
        WHERE empresa_id = %s
        """,
        (empresa_id,)
    )
    quantidade = cursor.fetchone()
    conexao.close()
    return quantidade


def metricas_gerais(empresa_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT
            COUNT(*) AS total_demandas,
            COALESCE(SUM(CASE WHEN status_demanda = 'aberta' THEN 1 ELSE 0 END), 0) AS abertas,
            COALESCE(SUM(CASE WHEN status_demanda = 'em_andamento' THEN 1 ELSE 0 END), 0) AS em_andamento,
            COALESCE(SUM(CASE WHEN status_demanda = 'concluida' THEN 1 ELSE 0 END), 0) AS concluidas,
            COALESCE(SUM(CASE WHEN status_demanda = 'cancelada' THEN 1 ELSE 0 END), 0) AS canceladas,
            CASE
                WHEN COUNT(*) = 0 THEN 0
                ELSE ROUND((SUM(CASE WHEN status_demanda = 'concluida' THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2)
            END AS percentual_conclusao
        FROM demandas
        WHERE empresa_id = %s
        """,
        (empresa_id,)
    )
    metricas = cursor.fetchone()
    conexao.close()
    return metricas
