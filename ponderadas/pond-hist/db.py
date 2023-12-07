import databases
import ormar
import sqlalchemy

from config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

# 1 - Tabela Usuário (User)
class User(ormar.Model):
    class Meta(BaseMeta):
        table_name = 'user'
    #Informações da tabela (User)
    Id: int = ormar.Integer(primary_key=True)
    Email: str = ormar.String(max_length=128, unique=True, nullable=False)
    password: str = ormar.String(max_length=16, nullable=False)
    

# 2 - Tabela Histórias (history)
class History(ormar.Model):
    class Meta(BaseMeta):
        table_name = 'history'
    #Informações
    id: int = ormar.Integer(primary_key=True)
    conteudo: str = ormar.String(max_length = 4000, nullable = False)

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)