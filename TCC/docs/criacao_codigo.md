# Documentacao da Criacao do Codigo

## 1. Visao Geral

O sistema foi desenvolvido como uma API utilizando Python com o framework FastAPI. A aplicacao tem como objetivo apoiar o gerenciamento de empresas, funcionarios, demandas, equipe, relatorios, dashboard, perfil e historico de alteracoes.

A estrutura do codigo foi organizada em camadas para separar responsabilidades e facilitar manutencao:

- `controllers`: definem as rotas da API.
- `services`: concentram as regras de negocio.
- `models`: executam as consultas e alteracoes no banco de dados.
- `schemas`: definem os dados esperados nas requisicoes.
- `utils`: contem funcoes auxiliares, como autenticacao, token, validacoes e criptografia.
- `database`: contem a conexao com o MySQL e o script de estrutura do banco.

## 2. Tecnologias Utilizadas

Foram utilizadas as seguintes tecnologias:

- Python
- FastAPI
- Uvicorn
- MySQL
- MySQL Connector
- JWT para autenticacao
- Bcrypt para criptografia de senhas
- Python Dotenv para variaveis de ambiente

## 3. Estrutura Principal da Aplicacao

O arquivo principal da API e o `app.py`. Nele a aplicacao FastAPI e criada e os roteadores sao registrados:

- empresas
- funcionarios
- autenticacao
- demandas
- equipe
- relatorios
- dashboard
- perfil

Essa organizacao permite que cada modulo do sistema tenha seu proprio controller, mantendo o arquivo principal mais simples.

## 4. Criacao dos Modulos

### 4.1 Empresas

O modulo de empresas permite cadastrar uma empresa no sistema. O cadastro valida:

- CNPJ
- email
- senha
- duplicidade de CNPJ
- duplicidade de email

Antes de salvar a empresa no banco de dados, a senha e criptografada com bcrypt.

### 4.2 Funcionarios

O modulo de funcionarios permite que uma empresa logada cadastre funcionarios. O funcionario fica associado a uma empresa por meio do campo `empresa_id`.

O cadastro valida:

- CPF
- email
- senha
- tipo de funcionario
- duplicidade de CPF
- duplicidade de email

Os tipos de funcionario permitidos sao:

- `adm`
- `usuario`

### 4.3 Autenticacao

A autenticacao foi implementada com JWT. Existem dois fluxos de login:

- login de empresa por CNPJ e senha
- login de funcionario por CPF e senha

Quando o login e realizado com sucesso, o sistema retorna um token de acesso. Esse token e usado nas rotas protegidas para identificar o usuario logado e aplicar regras de permissao.

### 4.4 Demandas

Foi criado um modulo especifico para demandas. Inicialmente foi considerado usar a tabela `movimentacoes`, mas posteriormente a estrutura foi alterada para uma tabela propria chamada `demandas`.

A demanda possui os principais campos:

- titulo
- descricao
- status
- setor
- cidade
- empresa vinculada
- funcionario responsavel
- data de criacao
- data de atualizacao
- data de conclusao

Os status permitidos sao:

- `aberta`
- `em_andamento`
- `concluida`
- `cancelada`

As rotas de demandas permitem:

- criar demanda
- listar demandas
- buscar demanda por ID
- editar demanda
- atualizar status
- cancelar demanda
- consultar historico da demanda

### 4.5 Historico de Demandas

Foi criada a tabela `historico_demandas` para registrar logs de acoes realizadas sobre uma demanda.

Sao registradas acoes como:

- criacao
- edicao
- alteracao de status
- cancelamento

Cada log armazena:

- demanda relacionada
- tipo do usuario
- ID do usuario
- acao realizada
- descricao
- data do historico

### 4.6 Equipe

O modulo de equipe permite visualizar informacoes relacionadas aos funcionarios da empresa.

Foram criadas rotas para:

- ver equipe
- listar funcionarios
- listar demandas da equipe
- consultar produtividade

A produtividade considera a quantidade de demandas por funcionario e o percentual de conclusao.

### 4.7 Relatorios

O modulo de relatorios concentra consultas gerenciais sobre as demandas e funcionarios.

Foram implementados relatorios de:

- demandas concluidas
- demandas pendentes
- quantidade de funcionarios
- metricas gerais

As metricas incluem totais por status e percentual de conclusao.

### 4.8 Dashboard

O dashboard foi criado para retornar uma visao resumida do sistema.

Ele retorna:

- estatisticas gerais
- cards
- numeros por status
- indicadores de produtividade

Esse retorno pode ser utilizado futuramente por uma interface visual.

### 4.9 Perfil

O modulo de perfil permite que empresa e funcionario visualizem e atualizem seus proprios dados.

Foram implementadas funcoes para:

- visualizar perfil
- editar perfil
- alterar senha

Para empresa, podem ser alterados:

- nome
- email
- nicho
- foto

Para funcionario, podem ser alterados:

- nome
- email
- setor
- foto

## 5. Banco de Dados

Foi criado um script SQL no arquivo `database/estrutura.sql`. Esse arquivo contem a estrutura das tabelas principais do sistema.

As tabelas incluem:

- empresas
- enderecos
- funcionarios
- estoques
- produtos
- lotes
- movimentacoes
- clientes
- enderecos_clientes
- demandas
- historico_demandas

A tabela `funcionarios` possui relacionamento com `empresas`, permitindo que cada funcionario pertenca a uma empresa.

A tabela `demandas` possui relacionamento com:

- empresa
- funcionario responsavel

A tabela `historico_demandas` possui relacionamento com a tabela `demandas`.

## 6. Variaveis de Ambiente

Foi utilizado um arquivo `.env` para armazenar configuracoes sensiveis e variaveis do sistema, como:

- host do banco
- usuario do banco
- senha do banco
- nome do banco
- porta do banco
- chave secreta JWT
- algoritmo JWT
- tempo de expiracao do token

Para evitar erro ao iniciar a API de pastas diferentes, foi criado o utilitario `env_util.py`, responsavel por carregar o `.env` com base no caminho real do projeto.

## 7. Organizacao das Permissoes

As permissoes foram organizadas a partir do token JWT.

Empresa:

- pode criar funcionarios
- pode criar, editar e cancelar demandas
- pode visualizar equipe, dashboard, relatorios e historico
- pode editar o proprio perfil

Funcionario administrador:

- pode criar, editar e cancelar demandas
- pode visualizar equipe, dashboard, relatorios e historico
- pode editar o proprio perfil

Funcionario usuario:

- pode visualizar as proprias demandas
- pode atualizar status das proprias demandas
- pode editar o proprio perfil

## 8. Consideracoes Sobre a Implementacao

Durante a criacao do codigo, a API foi evoluindo por etapas. Primeiro foram estruturados cadastro, login e autenticacao. Em seguida foram adicionados os modulos de demandas, logs, equipe, relatorios, dashboard e perfil.

Essa abordagem permitiu construir o sistema de forma incremental, validando cada parte antes de seguir para a proxima.
