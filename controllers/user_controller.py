from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()


    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)


    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)


    def register(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/register")
        else:
            self.user_service.save()
            return self.redirect('/home')


    def login(self):
        if request.method == 'GET':
            return self.render('login')
        else:
            session = request.environ['beaker.session']
            email = request.forms.get("email")
            password = request.forms.get("password")

            user, error = self.user_service.login_user(email, password)
            if error:
                return self.render('login', error=error)

            session['user_id'] = user.user_id
            session['logged_in'] = True
            session.save()
            return redirect('/home')


    def logout(self):
        if request.method == 'GET':
            session = request.environ['beaker.session']
            session.delete()
            return redirect('/login')
        else:
            return redirect('/home')


    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            self.user_service.edit_user(user)
            return self.redirect('/users')


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
