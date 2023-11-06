from flask import Flask
from routes.user import router as user_router


app = Flask(__name__)

# Rotas para animais
app.register_blueprint(user_router)

app.run(port=5000)