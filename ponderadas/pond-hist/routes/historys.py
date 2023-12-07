from fastapi import APIRouter, Body
from db import database, History
from model import HistSchema

app = APIRouter(tags=["hist"])

@app.get("/", tags=["hist"])
async def read_hist():
    if not database.is_connected:
        await database.connect()
        
    return await History.objects.all()

@app.post("/env", tags=["hist"])
async def write_hist(hist :HistSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()
    