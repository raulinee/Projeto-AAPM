from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.auth import get_usuario_opcional

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

@app.get("/")
def tela_inicial(
    request: Request,
    usuario = Depends(get_usuario_opcional)
):
    #Tela não logado
    if usuario is None:
        return templates.TemplateResponse(
            request,
            "/auth/login.html",
            {"request": request}
        )
    #logado - exibir a tela de funcionario
    return templates.TemplateResponse(
        request,
        "home.html",
        {"request": request, "usuario": usuario}
    )

@app.get("/painel", response_class=HTMLResponse)
async def painel(request: Request):

    return templates.TemplateResponse(
        request,
        "painel.html",
        {"request": request}
    )

@app.get("/usuarios", response_class=HTMLResponse)
async def usuarios_redirect():
    return RedirectResponse(url="/usuarios/")