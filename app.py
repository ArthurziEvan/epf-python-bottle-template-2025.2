import uuid

from beaker.middleware import SessionMiddleware
from bottle import Bottle, run
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.session_opts = {
            'session.key': 'projeto-python-amigo-oculto-oo-2025-2',
            'session.lock_dir': './data/session_locks',
            'session.cookie_expires': True,
            'session.type': 'file',
            'session.data_dir': './data/sessions',
            'session.auto': True,
            'session.secret': pbkdf2_sha256.hash(self.config.SECRET_KEY),
            'session.encrypt_key': str(uuid.uuid4()),

            'session.validate_key': self.config.SECRET_KEY
        }
        self.app = SessionMiddleware(self.bottle, self.session_opts)

    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)


    def run(self):
        self.setup_routes()
        run(
            app=self.app,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()