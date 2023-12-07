from fastapi import APIRouter, Body
from db import database, User
from model import UserSchema, LoginUserSchema

app = APIRouter(tags=["user"])

@app.get("/", tags=["user"])
async def read_users():
    if not database.is_connected:
        await database.connect()
        
    return await User.objects.all()

@app.post("/", tags=["user"])
async def sing_up(user: UserSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()
        
    await User.objects.create(Email=user.Email,
                              password=user.password)
    # return signJWT()
    
async def check_user(data: LoginUserSchema):
    if not database.is_connected:
        await database.connect()
    
    users = await User.objects.all()
    for user in users:
        if user.Email == data.Email and user.password == data.password:
            return True
    return False

@app.post("/login", tags=["user"])
async def user_login(user: UserSchema = Body(default=None)):
    return {"error"}