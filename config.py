import os

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Configurações do servidor
    HOST = 'localhost'
    PORT = 8080
    DEBUG = True
    RELOADER = True

    # Paths
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    # Outras configurações
    SECRET_KEY = '762r3gy8234rhu94r3j89fj8934rj8934rj894r3j8934rj8934j9834f89j4f398j34f8u934fj8934fj89'