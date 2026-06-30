# Documentacao dos Testes e Tratamento de Erros

## 1. Visao Geral

Esta documentacao descreve os testes realizados na API e os principais tratamentos de erro implementados durante o desenvolvimento.

Os testes foram realizados localmente com a API executando em:

```text
http://127.0.0.1:8000
```

A documentacao interativa da API foi acessada em:

```text
http://127.0.0.1:8000/docs
```

## 2. Testes Iniciais

Primeiro foi verificado se a API estava respondendo corretamente.

Foram testados:

- carregamento da documentacao `/docs`
- carregamento do arquivo OpenAPI `/openapi.json`
- listagem das rotas registradas
- acesso a rotas protegidas sem token

Resultado:

- `/docs` respondeu com status `200 OK`
- `/openapi.json` carregou corretamente
- as rotas principais apareceram registradas
- rotas protegidas retornaram `401`, como esperado

## 3. Rotas Identificadas nos Testes

Durante os testes, foram identificadas as seguintes rotas principais:

```text
POST   /empresas/empresa/criar
POST   /funcionarios/funcionario/criar
POST   /auth/logar/empresa
POST   /auth/logar/funcionario
POST   /demandas/criar
GET    /demandas
GET    /demandas/{demanda_id}
PUT    /demandas/{demanda_id}
PATCH  /demandas/{demanda_id}/status
DELETE /demandas/{demanda_id}
GET    /demandas/{demanda_id}/historico
GET    /equipe
GET    /equipe/funcionarios
GET    /equipe/demandas
GET    /equipe/produtividade
GET    /relatorios/demandas-concluidas
GET    /relatorios/demandas-pendentes
GET    /relatorios/quantidade-funcionarios
GET    /relatorios/metricas
GET    /dashboard
GET    /perfil
PUT    /perfil
PATCH  /perfil/senha
```

## 4. Testes com Dados Reais

Depois dos testes iniciais, foram criados registros de teste no banco local.

O fluxo principal testado foi:

1. Criar empresa.
2. Realizar login da empresa.
3. Criar funcionario administrador.
4. Realizar login do funcionario.
5. Visualizar perfil do funcionario.
6. Criar demanda.
7. Listar demandas.
8. Atualizar status da demanda.
9. Consultar historico da demanda.
10. Consultar dashboard.
11. Consultar equipe.
12. Consultar relatorios.
13. Visualizar perfil da empresa.

Resultado:

```text
Fluxo principal OK
```

## 5. Testes Extras

Alem do fluxo principal, tambem foram testadas operacoes complementares:

1. Editar demanda.
2. Alterar status para concluida.
3. Consultar relatorio de demandas concluidas.
4. Editar perfil da empresa.
5. Alterar senha da empresa.
6. Realizar login com a nova senha.
7. Cancelar demanda.
8. Consultar logs do historico.

Resultado:

```text
Fluxo extra OK
Logs funcionando
Dashboard funcionando
Relatorios funcionando
Perfil funcionando
```

## 6. Tratamento de Erros de Autenticacao

As rotas protegidas utilizam JWT para identificar o usuario logado.

Quando uma rota protegida e acessada sem token, a API retorna erro `401`.

Esse comportamento foi testado nas rotas:

- `/dashboard`
- `/demandas`
- `/perfil`

Resultado esperado:

```text
401 Unauthorized
```

## 7. Tratamento de Erros de Permissao

O sistema possui regras diferentes para empresa, funcionario administrador e funcionario usuario.

Exemplos de regras:

- apenas empresa ou funcionario administrador podem criar demandas
- apenas empresa ou funcionario administrador podem editar ou cancelar demandas
- funcionario usuario so pode visualizar e atualizar as proprias demandas
- apenas empresa ou funcionario administrador podem visualizar historico, equipe, dashboard e relatorios

Quando um usuario tenta acessar uma funcao sem permissao, a API retorna erro `403`.

## 8. Tratamento de Erros de Validacao

O sistema valida os dados antes de cadastrar ou atualizar informacoes.

Validacoes implementadas:

- CPF deve conter somente numeros e ter 11 digitos
- CNPJ deve conter somente numeros e ter 14 digitos
- email deve conter `@` e `.`
- senha deve ter pelo menos 8 caracteres
- senha deve conter letra maiuscula
- senha deve conter letra minuscula
- senha deve conter numero
- senha deve conter caractere especial
- tipo de funcionario deve ser `adm` ou `usuario`
- status da demanda deve ser valido

Quando uma validacao falha, a API retorna erro `400`.

## 9. Tratamento de Erros de Duplicidade

Foram implementadas verificacoes para evitar cadastros duplicados.

O sistema verifica:

- CNPJ de empresa ja cadastrado
- email de empresa ja cadastrado
- CPF de funcionario ja cadastrado
- email de funcionario ja cadastrado

Quando um dado duplicado e identificado, a API retorna erro `409`.

## 10. Tratamento de Erros de Login

No login de empresa e funcionario, o sistema verifica se o usuario existe e se a senha esta correta.

Erros tratados:

- empresa nao encontrada
- funcionario nao encontrado
- senha incorreta

Quando o usuario nao existe, a API retorna erro `404`.

Quando a senha esta incorreta, a API retorna erro `401`.

## 11. Tratamento de Erros de Demanda

As demandas possuem validacoes e regras especificas.

Erros tratados:

- demanda nao encontrada
- demanda pertencente a outra empresa
- status invalido
- tentativa de editar sem enviar campos
- tentativa de usuario comum acessar demanda de outro funcionario

Os principais codigos retornados sao:

- `400` para dados invalidos
- `403` para acesso proibido
- `404` para demanda inexistente

## 12. Erros Encontrados Durante os Testes

Durante os testes, alguns erros foram encontrados e corrigidos.

### 12.1 Erro ao iniciar a API pelo caminho incorreto

Erro:

```text
Could not import module "app"
```

Causa:

O comando do Uvicorn estava sendo executado em uma pasta diferente da pasta onde o arquivo `app.py` estava localizado.

Solucao:

Executar o comando dentro da pasta correta:

```text
C:\Users\Pichau\Documents\TCC\TCC\TCC
```

Ou usar `--app-dir` apontando para essa pasta.

### 12.2 Erro ao importar controllers

Erro:

```text
ModuleNotFoundError: No module named 'controllers'
```

Causa:

O Python nao estava localizando as pastas internas da API por causa do diretorio de execucao.

Solucao:

Rodar o servidor a partir da pasta correta da API.

### 12.3 Erro ao carregar variaveis de ambiente

Erro:

```text
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
```

Causa:

A variavel `ACCESS_TOKEN_EXPIRE_MINUTES` nao estava sendo carregada do `.env`.

Solucao:

Foi criado o arquivo `utils/env_util.py`, que carrega o `.env` usando o caminho real do projeto.

### 12.4 Erro na criptografia de senha

Erro:

```text
Internal Server Error
```

Causa:

O cadastro de empresa falhava por incompatibilidade entre `passlib`, `bcrypt` e a versao do Python utilizada.

Solucao:

O arquivo `utils/criptografia_util.py` foi alterado para utilizar `bcrypt` diretamente.

### 12.5 Erro no token do funcionario

Erro:

```text
Demanda pertence a outra empresa
```

Causa:

Apos adicionar o campo `foto_funcionario`, o indice usado para montar o token do funcionario ficou incorreto. O `empresa_id` estava sendo lido da posicao errada.

Solucao:

O arquivo `services/auth_service.py` foi corrigido para usar o indice correto do `empresa_id`.

## 13. Verificacao Final

Apos as correcoes, foi executada a verificacao de sintaxe do projeto:

```text
python -m compileall .
```

Resultado:

```text
Sem erros de compilacao
```

Tambem foi realizado novo teste completo pela API, com resultado positivo.

## 14. Conclusao dos Testes

Os testes confirmaram que os principais fluxos da API estao funcionando:

- autenticacao
- cadastro de empresa
- cadastro de funcionario
- demandas
- historico
- dashboard
- equipe
- relatorios
- perfil
- alteracao de senha
- tratamento de erros de acesso e validacao

As falhas encontradas durante os testes foram corrigidas, tornando a API mais estavel para continuidade do desenvolvimento.
