from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.usuarios import Usuario
from app.auth import hash_senha, verificar_senha, criar_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])


templates = Jinja2Templates(directory="app/templates")


@router.get("/login", response_class=HTMLResponse)
def tela_login(request: Request):
    return templates.TemplateResponse(
        request,
        "auth/login.html", 
        {"request": request}
        )



@router.post("/login")
def fazer_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    # Busca o usuário no banco de dados
    usuario = db.query(Usuario).filter_by(email=email).first()
    
    #2. Verificar a senha com bcrypt
    senha_correta = (
        usuario is not None and verificar_senha(senha, usuario.senha_hash)
    )

    if not senha_correta:
        return templates.TemplateResponse(
            request,
            "auth/login.html",
            {
                "request": request,
                "erro": "E-mail ou senha incorretos"
            }
        )

    # Verificar se o usuário está ativo

    if not usuario.ativo:
        return templates.TemplateResponse(
            request,
            "auth/login.html",
            {
                "request": request,
                "erro": "Usuário inativo. Contate o administrador."
            }
        )
    
    # Criar token JWT
    token_data = {
        "sub": usuario.email,
        "nome": usuario.nome,
        "role": usuario.role,
        "id": usuario.id

    }

    token = criar_token(token_data)
    

    # 4. Salvar o token em um cookie e redirecionar para página home
    response = RedirectResponse(url="/", status_code=302)

    #define p cookie com o token jwt
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=3600,  #Expira em 1 hora
        samesite="Lax"
    )
    return response

@router.get("/logout")
def sair():
    response = RedirectResponse(url="/auth/login", status_code=302)
    response.delete_cookie(key="access_token")
    return response