from flask import Blueprint, render_template
from controller import valor_retorno

cadastro_router = Blueprint('/home', template_folder="./templates")

class HomeController:
    valor: int
    juros: float

@cadastro_router.route('/')
def home(data = service):
    
    token = valor_retorno(valor, juros)
    
    return render_template('home.html', token)