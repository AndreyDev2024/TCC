from database.conexao import conectar


def listar_funcionarios_por_empresa(empresa_id):
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
            empresa_id
        FROM funcionarios
        WHERE empresa_id = %s
        ORDER BY nome_funcionario
        """,
        (empresa_id,)
    )
    funcionarios = cursor.fetchall()
    conexao.close()
    return funcionarios


def listar_demandas_da_equipe(empresa_id):
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
        ORDER BY d.data_criacao DESC
        """,
        (empresa_id,)
    )
    demandas = cursor.fetchall()
    conexao.close()
    return demandas


def produtividade_por_funcionario(empresa_id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT
            f.id_funcionario,
            f.nome_funcionario,
            f.setor_funcionario,
            COUNT(d.id_demanda) AS total_demandas,
            SUM(CASE WHEN d.status_demanda = 'concluida' THEN 1 ELSE 0 END) AS demandas_concluidas,
            SUM(CASE WHEN d.status_demanda != 'concluida' THEN 1 ELSE 0 END) AS demandas_nao_concluidas,
            CASE
                WHEN COUNT(d.id_demanda) = 0 THEN 0
                ELSE ROUND((SUM(CASE WHEN d.status_demanda = 'concluida' THEN 1 ELSE 0 END) / COUNT(d.id_demanda)) * 100, 2)
            END AS percentual_conclusao
        FROM funcionarios f
        LEFT JOIN demandas d
            ON d.funcionario_id = f.id_funcionario
            AND d.empresa_id = f.empresa_id
        WHERE f.empresa_id = %s
        GROUP BY f.id_funcionario, f.nome_funcionario, f.setor_funcionario
        ORDER BY demandas_concluidas DESC, f.nome_funcionario
        """,
        (empresa_id,)
    )
    produtividade = cursor.fetchall()
    conexao.close()
    return produtividade
