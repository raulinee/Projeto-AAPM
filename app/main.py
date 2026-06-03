from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.auth import get_usuario_opcional, get_admin

from app.controllers import auth_controller
from app.controllers import usuario_controller
from app.controllers import categoria_controller
from app.controllers import produto_controller

app = FastAPI(title="Projeto AAPM")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(auth_controller.router)
app.include_router(usuario_controller.router)
app.include_router(categoria_controller.router)
app.include_router(produto_controller.router)

from sqlalchemy.orm import Session
from app.database import get_db
from app.models.produto import Produto
from app.models.categoria import Categoria

@app.get("/")
def tela_inicial(
    request: Request,
    usuario = Depends(get_usuario_opcional),
    db: Session = Depends(get_db)
):
    #Tela não logado
    if usuario is None:
        return templates.TemplateResponse(
            request,
            "/auth/login.html",
            {"request": request}
        )
    
    # Buscar produtos e categorias
    produtos = db.query(Produto).filter(Produto.ativo == True).all()
    categorias = db.query(Categoria).filter(Categoria.ativo == True).all()

    #logado - exibir a tela de funcionario
    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "request": request, 
            "usuario": usuario,
            "produtos": produtos,
            "categorias": categorias
        }
    )

@app.get("/painel", response_class=HTMLResponse)
async def painel(
    request: Request,
    admin = Depends(get_admin)
):
    return templates.TemplateResponse(
        request,
        "painel/index.html",
        {"request": request, "usuario": admin}
    )

@app.get("/usuarios", response_class=HTMLResponse)
async def usuarios_redirect():
    return RedirectResponse(url="/usuarios/")