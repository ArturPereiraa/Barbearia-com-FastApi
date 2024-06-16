


import uvicorn
from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from models.models import Base, Agendamento, Usuario
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Configura o diretório de templates HTML
templates = Jinja2Templates(directory="templates")

# Adiciona middleware de sessão
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para página inicial
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para a página de agendamento
@app.get("/agendamento", response_class=HTMLResponse)
async def read_agendamento(request: Request):
    return templates.TemplateResponse("agendamento.html", {"request": request})







@app.post("/agendar", response_class=HTMLResponse)
async def agendar(request: Request, nome: str = Form(...), data: str = Form(...), hora: str = Form(...), db: Session = Depends(get_db)):
    user_email = request.session.get('user_email')
    if not user_email:
        return RedirectResponse(url="/login?message=Realize o login para fazer um agendamento", status_code=303)

    usuario = db.query(Usuario).filter(Usuario.email == user_email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    try:
        data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
        hora_formatada = datetime.strptime(hora, "%H:%M").time()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data ou hora inválido")

    agendamento = Agendamento(nome=nome, data=data_formatada, hora=hora_formatada, usuario_id=usuario.id)

    db.add(agendamento)
    db.commit()
    db.refresh(agendamento)

    return templates.TemplateResponse("agendamento.html", {"request": request, "message": "Agendamento realizado com sucesso!"})



# Rota para a página de cortes
@app.get("/cortes", response_class=HTMLResponse)
async def read_cortes(request: Request):
    return templates.TemplateResponse("cortes.html", {"request": request})

# Rota para a página de cadastro
@app.get("/cadastro", response_class=HTMLResponse)
async def read_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

# Rota POST para registrar novo usuário
@app.post("/registrar", response_class=HTMLResponse)
async def registrar(request: Request, nome: str = Form(...), email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario_existente:
        return templates.TemplateResponse("cadastro.html", {"request": request, "message": "Email já está em uso", "message_class": "error"})

    novo_usuario = Usuario(nome=nome, email=email, senha=senha)

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return RedirectResponse(url="/login", status_code=303)

# Rota para login 
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request, message: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "message": message})

# Rota para processar o login
@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or usuario.senha != senha:
        return templates.TemplateResponse("login.html", {"request": request, "message": "Email ou senha incorretos", "message_class": "error"})

    # Armazena o email do usuário na sessão
    request.session['user_email'] = email

    # Redireciona para a página inicial após o login bem-sucedido
    return RedirectResponse(url="/", status_code=303)

# Rota para fazer logout
@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session.pop('user_email', None)  # Remove o email do usuário da sessão
    return RedirectResponse(url="/login", status_code=303)

# Rota para a página de perfil
@app.get("/perfil", response_class=HTMLResponse)
async def perfil(request: Request, db: Session = Depends(get_db)):
    user_email = request.session.get('user_email')
    if not user_email:
        return RedirectResponse(url="/login", status_code=303)

    # Busca o usuário no banco de dados pelo email
    usuario = db.query(Usuario).filter(Usuario.email == user_email).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Dados do usuário para passar para o template
    dados_usuario = {
        "nome": usuario.nome,
        "email": usuario.email,
    }

    return templates.TemplateResponse("perfil.html", {"request": request, "usuario": dados_usuario})

# Monta os arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")





@app.get("/meus_agendamentos", response_class=HTMLResponse)
async def meus_agendamentos(request: Request, db: Session = Depends(get_db)):
    user_email = request.session.get('user_email')
    if not user_email:
        return RedirectResponse(url="/login", status_code=303)

    # Busca o usuário pelo email
    usuario = db.query(Usuario).filter(Usuario.email == user_email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Busca todos os agendamentos associados ao usuário
    agendamentos = db.query(Agendamento).filter(Agendamento.usuario_id == usuario.id).all()

    return templates.TemplateResponse("meus_agendamentos.html", {"request": request, "usuario": usuario, "agendamentos": agendamentos})



# Executa o servidor Uvicorn
if __name__ == "__main__":
    uvicorn.run(app)




