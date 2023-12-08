from fastapi import APIRouter, Body
from db import database, History
from model import HistSchema
from chat_openai import chat_whit_gpt

app = APIRouter(prefix="/hist", tags=["hist"])

@app.get("/", tags=["hist"])
async def read_hist():
    if not database.is_connected:
        await database.connect()
        
    return await History.objects.all()

@app.post("/env", tags=["hist"])
async def write_hist(hist: HistSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()
    
    new_history = chat_whit_gpt(hist.conteudo)
    
    print("Nova história: ", new_history)
    
    return await History.objects.create(conteudo=new_history)