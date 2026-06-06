from fastapi import FastAPI
from controllers.auth_controller import auth_router
from controllers.funcionario_controller import funcionarios_router
from controllers.empresa_controller import empresas_router

app = FastAPI()
app.include_router(empresas_router)
app.include_router(funcionarios_router)
app.include_router(auth_router)

#uvicorn app:app --reload