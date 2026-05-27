from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuarios import Usuario
from app.auth import get_admin, hash_senha

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def listar_usuario(
    resquest: Request,
    db: Session = Depends(get_db),
    admin = Depends(get_admin) #Bloqueia quem não é admin
):
    
    # Buscar todos os usuario do banco
    usuarios = db.query(Usuario).order_by(Usuario.nome).all()

    return templates.TemplateResponse(
        resquest,
        "usuarios/index.html",
        {   
            "resquest": resquest, 
            "usuarios": usuarios, #lista para exibir na tabela
            "admin": admin # Dados de quem esta logado
        }
    )