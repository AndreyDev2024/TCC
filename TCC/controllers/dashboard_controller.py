from fastapi import APIRouter, Depends

from services.dashboard_service import dashboard
from utils.dependecies import usuario_logado


dashboard_router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@dashboard_router.get("")
async def ver_dashboard(usuario=Depends(usuario_logado)):
    return dashboard(usuario)
