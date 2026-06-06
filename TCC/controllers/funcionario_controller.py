from fastapi import APIRouter
from schemas.funcionario_schema import CriarFuncionario
from services.funcionario_service import criar_funcionario

funcionarios_router = APIRouter(prefix='/funcionarios', tags=['Funcionario'])
@funcionarios_router.post('/funcionario/criar')
async def cadastrarFUNCIONARIO(dados: CriarFuncionario):
    resultado = criar_funcionario(
        nome = dados.nome,
        cpf = dados.cpf,
        email = dados.email,
        senha = dados.senha,
        tipo = dados.tipo,
        setor = dados.setor   
    )
    return resultado