from fastapi import FastAPI
from controllers.auth_controller import auth_router
from controllers.funcionario_controller import funcionarios_router
from controllers.empresa_controller import empresas_router
from controllers.demanda_controller import demandas_router
from controllers.dashboard_controller import dashboard_router
from controllers.equipe_controller import equipe_router
from controllers.perfil_controller import perfil_router
from controllers.relatorio_controller import relatorios_router

app = FastAPI()
app.include_router(empresas_router)
app.include_router(funcionarios_router)
app.include_router(auth_router)
app.include_router(demandas_router)
app.include_router(equipe_router)
app.include_router(relatorios_router)
app.include_router(dashboard_router)
app.include_router(perfil_router)

#uvicorn app:app --reload
