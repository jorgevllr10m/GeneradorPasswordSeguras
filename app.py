from flask import Flask
from api.password import web

def create_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    return app

app = create_app()

if __name__ == "__main__":
    app.run()