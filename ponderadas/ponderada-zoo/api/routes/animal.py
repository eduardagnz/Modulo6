from flask import Blueprint
from prisma import Prisma
from models.animal import AnimalSchema

router = Blueprint('/animal', __name__)


# Rota create
@router.post('/')
async def create_animal(data: AnimalSchema) -> dict:
    
    db = Prisma
    await db.connect()
    
    
    
    
    
    return "new animal"

# Rota read
@router.get('/<id>')
def get_animal(id: int) -> str:
    return f"animal {id}"

# Rota update
@router.put('/<id>')
def update_animal(id: int) -> str:
    return f"animal {id} updated with success"

# Rota delete
@router.delete('/<id>')
def delete_animal(id: int) -> str:
    return f"animal {id} deleted"

