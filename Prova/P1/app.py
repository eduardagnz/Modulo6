from flask import Flask
from router.cadastro.view import valor_router 
# from routes.home.view import home_router

app = Flask()

# app.register_blueprint(login_router)
app.register_blueprint(valor_router)

app.run(debug=True, port= 3000)