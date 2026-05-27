from app.database import Session
from app.models.usuarios import Usuario
from app.auth import hash_senha

# Funcao para cadastrar os usuario
def seed():
    db = Session()
    try:
        nome_usuario = "operador"
        email_usuario = "operador@teste.com.br"
        senha_usuario = "operador@12345"
        perfil = "operador"


        # Verificar se o usuário já existe
        existente = db.query(Usuario).filter_by(email= email_usuario).first()

        if  not existente:
            # Criar o usuário
            usuario = Usuario(
                nome=nome_usuario,
                email=email_usuario,
                senha_hash=hash_senha(senha_usuario),
                role=perfil
            )
            db.add(usuario)
            db.commit()
            print(f"Usuário cadastrado com sucesso: {nome_usuario}")
        else:
            print(f"este e-mail já está cadastrado!")
    except Exception as erro:
        db.rollback()
        print(f"Erro: {erro}")
    finally:
        db.close()


seed()