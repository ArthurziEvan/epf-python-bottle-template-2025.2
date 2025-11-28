from beaker.middleware import SessionMiddleware
from bottle import Bottle, run
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.session_opts = {
            'session.type': 'cookie',
            'session.cookie_expires': 7200,
            'session.auto': True,

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
