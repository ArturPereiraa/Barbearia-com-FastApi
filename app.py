
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from models.models import Base
from crud.crud import get_users, create_user
from database.connection import SessionLocal, engine  

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Rota para a página principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    users = get_users(SessionLocal())
    return templates.TemplateResponse("index.html", {"request": request, "users": users})


# Rota para a página cortes

@app.get("/cortes", response_class=HTMLResponse)  
async def read_cortes(request: Request):
    return templates.TemplateResponse("cortes.html", {"request": request})

uvicorn.run(app)