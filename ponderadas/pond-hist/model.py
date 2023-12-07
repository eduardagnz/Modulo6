from pydantic import BaseModel, Field, EmailStr 

# Classe de usuários
class UserSchema(BaseModel):
    id: int = Field(default=None, gt=0)
    Email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    
    class Config:
        schema_extra = {
            "schema_user": {
                "Email" : "adm@mail.com",
                "password" : "123"
            }
        }
# Classe de Login
class LoginUserSchema(BaseModel):
    Email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    
    class Config:
        schema_extra = {
            "user_teste" : {
                "Email": "teste@mail.com",
                "password":"123"
            }
        }
        
#Classe de Histórias
class HistSchema(BaseModel):
    id: int = Field(default=None, gt = 0)
    conteudo: str = Field(default=None)
    
    class Config:
        schema_extra = {
            "post_teste" : {
                "conteudo" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt praesent semper feugiat nibh sed pulvinar proin. Suspendisse faucibus interdum posuere lorem ipsum dolor sit amet consectetur. Purus in mollis nunc sed id semper risus in."
            }
        }