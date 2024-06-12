
# import uvicorn
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from sqlalchemy.orm import Session
# from models.models import Base
# from crud.crud import get_users, create_user
# from database.connection import SessionLocal, engine  

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")

# # Rota para a página principal
# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     users = get_users(SessionLocal())
#     return templates.TemplateResponse("index.html", {"request": request, "users": users})


# # Rota para a página cortes

# @app.get("/cortes", response_class=HTMLResponse)  
# async def read_cortes(request: Request):
#     return templates.TemplateResponse("cortes.html", {"request": request})


# # Rota para a página agendamento

# @app.get("/agendamento", response_class=HTMLResponse)  
# async def read_cortes(request: Request):
#     return templates.TemplateResponse("agendamento.html", {"request": request})




# import uvicorn
# from fastapi import FastAPI, Form, Request, Depends, HTTPException
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
# from datetime import datetime
# from models.models import Base, Agendamento  # Importar os modelos

# # Inicializa a aplicação FastAPI
# app = FastAPI()

# # Configuração do banco de dados
# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Mover a chamada para criar as tabelas após a definição dos modelos
# Base.metadata.create_all(bind=engine)

# # Configura o diretório de templates HTML
# templates = Jinja2Templates(directory="templates")

# # Função para obter a sessão do banco de dados
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Rota GET para exibir o formulário de agendamento
# @app.get("/", response_class=HTMLResponse)
# async def read_form(request: Request):
#     return templates.TemplateResponse("agendamento.html", {"request": request})

# # Rota POST para processar o agendamento
# @app.post("/agendar")
# async def agendar(nome: str = Form(...), data: str = Form(...), hora: str = Form(...), db: Session = Depends(get_db)):
#     try:
#         # Formata a data e a hora recebidas
#         data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
#         hora_formatada = datetime.strptime(hora, "%H:%M").time()
#     except ValueError:
#         # Lança uma exceção HTTP se a data ou hora estiverem em um formato inválido
#         raise HTTPException(status_code=400, detail="Formato de data ou hora inválido")
    
#     # Cria um novo objeto de agendamento
#     agendamento = Agendamento(nome=nome, data=data_formatada, hora=hora_formatada)
    
#     # Adiciona o agendamento ao banco de dados e confirma a transação
#     db.add(agendamento)
#     db.commit()
#     db.refresh(agendamento)
    
#     return {"message": "Agendamento realizado com sucesso!"}

# # Executa o servidor Uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app)

import uvicorn
from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from models.models import Base, Agendamento  # Importar os modelos

# Inicializa a aplicação FastAPI
app = FastAPI()

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Mover a chamada para criar as tabelas após a definição dos modelos
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

# Rota GET para exibir o formulário de agendamento

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("agendamento.html", {"request": request})

# Rota POST para processar o agendamento

@app.post("/agendar")
async def agendar(nome: str = Form(...), data: str = Form(...), hora: str = Form(...), db: Session = Depends(get_db)):
    try:
        # Formata a data e a hora recebidas

        data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
        hora_formatada = datetime.strptime(hora, "%H:%M").time()
    except ValueError:

        # Lança uma exceção HTTP se a data ou hora estiverem em um formato inválido

        raise HTTPException(status_code=400, detail="Formato de data ou hora inválido")
    
    # Cria um novo objeto de agendamento
    agendamento = Agendamento(nome=nome, data=data_formatada, hora=hora_formatada)
    
    # Adiciona o agendamento ao banco de dados e confirma a transação

    db.add(agendamento)
    db.commit()
    db.refresh(agendamento)
    
    return {"message": "Agendamento realizado com sucesso!"}


app.mount("/static", StaticFiles(directory="static"), name="static")

# Rota para a página principal

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    users = get_users(SessionLocal())
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

# Rota para a página cortes

@app.get("/cortes", response_class=HTMLResponse)  
async def read_cortes(request: Request):
    return templates.TemplateResponse("cortes.html", {"request": request})


# Rota para a página agendamento
@app.get("/agendamento", response_class=HTMLResponse)  
async def read_agendamento(request: Request):
    return templates.TemplateResponse("agendamento.html", {"request": request})



# Executa o servidor Uvicorn
if __name__ == "__main__":
    uvicorn.run(app)  
