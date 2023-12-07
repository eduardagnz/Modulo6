from fastapi import FastAPI
from db import database, User, History

from routes.users import app as user_router
from routes.historys import app as history_router

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(user_router)
app.include_router(history_router)

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
        
@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()