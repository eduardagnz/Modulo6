from flask import Blueprint
from prisma import Prisma
from models.user import UserSchema

router = Blueprint('/user', __name__)

@router.post('/singup')
async def create(data: UserSchema) -> dict:
    db = Prisma
    await db.connect()
    
    try:
        user = await db.user.create(
            {
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "money": 100
            }
        )
    except Exception as e:
        raise f"Error creating user: {str(e)}"
    
    return {
        "request": "Success",
        "data": data
    }    
    