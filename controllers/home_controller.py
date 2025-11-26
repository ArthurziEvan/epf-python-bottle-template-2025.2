from bottle import Bottle

from controllers.base_controller import BaseController


class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()

    # Rotas Sala
    def setup_routes(self):
        self.app.route('/home', method='GET', callback=self.show_home)

    def show_home(self):
        return self.render('home')

home_routes = Bottle()
home_controller = HomeController(home_routes)