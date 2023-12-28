from .configurations.Cors import init_cors
from flask import Flask

def create_app():
    api = Flask(__name__)

    #Iniciando as configurações da API
    init_cors(api)

    return api