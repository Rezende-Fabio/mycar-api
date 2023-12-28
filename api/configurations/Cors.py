from flask_cors import CORS

def init_cors(api):
    cors = CORS()
    cors.init_app(api)
    