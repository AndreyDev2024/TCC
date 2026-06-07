from fastapi import APIRouter, Depends
from schemas.funcionario_schema import CriarFuncionario
from services.funcionario_service import criar_funcionario
from utils.dependecies import empresa_logada

funcionarios_router = APIRouter(prefix='/funcionarios', tags=['Funcionario'])
@funcionarios_router.post('/funcionario/criar')
async def cadastrarFUNCIONARIO(dados: CriarFuncionario, empresa = Depends(empresa_logada)):
    resultado = criar_funcionario(
        nome = dados.nome,
        cpf = dados.cpf,
        email = dados.email,
        senha = dados.senha,
        tipo = dados.tipo,
        setor = dados.setor,
        empresa_id = empresa['id'],
    )
    return resultado