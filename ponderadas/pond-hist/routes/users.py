from fastapi import APIRouter, Body
from db import database, User
from model import UserSchema, LoginUserSchema

app = APIRouter(prefix="/users", tags=["user"])

@app.get("/", tags=["user"])
async def read_users():
    if not database.is_connected:
        await database.connect()
        
    return await User.objects.all()

@app.post("/", tags=["user"])
async def sing_up(user: UserSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()
        
    return await User.objects.create(Email=user.Email,
                              password=user.password)
@user_app.put("/")
async def update_user(new_user: UserSchema = Body(default=None)):
  if not database.is_connected:
    await database.connect()
  
  return await User.objects.update_or_create(Email=new_user.Email, password=new_user.password)