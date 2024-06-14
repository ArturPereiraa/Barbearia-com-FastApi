

import uvicorn
from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from models.models import Base, Agendamento, Usuario

app = FastAPI()

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Configura o diretório de templates HTML
templates = Jinja2Templates(directory="templates")

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

# Rota POST para agendar
@app.post("/agendar")
async def agendar(nome: str = Form(...), data: str = Form(...), hora: str = Form(...), db: Session = Depends(get_db)):
    try:
        data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
        hora_formatada = datetime.strptime(hora, "%H:%M").time()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data ou hora inválido")

    agendamento = Agendamento(nome=nome, data=data_formatada, hora=hora_formatada)

    db.add(agendamento)
    db.commit()
    db.refresh(agendamento)

    return {"message": "Agendamento realizado com sucesso!"}

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
        # Renderiza o template cadastro.html com a mensagem de erro
        return templates.TemplateResponse("cadastro.html", {"request": request, "message": "Email já está em uso", "message_class": "error"})

    novo_usuario = Usuario(nome=nome, email=email, senha=senha)

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return RedirectResponse(url="/login", status_code=303)
 

# Rota para exibir o formulário de login
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "message": None})

# Rota para processar o login
@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or usuario.senha != senha:
        return templates.TemplateResponse("login.html", {"request": request, "message": "Email ou senha incorretos", "message_class": "error"})

    # Redireciona para a página inicial após o login bem-sucedido
    return RedirectResponse(url="/", status_code=303)

# Monta os arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Executa o servidor Uvicorn
if __name__ == "__main__":
    uvicorn.run(app)


