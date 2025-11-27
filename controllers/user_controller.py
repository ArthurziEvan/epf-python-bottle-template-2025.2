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
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)


    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)


    def register(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/register")
        else:
            try:
                new_user = self.user_service.save() 
                
                session = request.environ['beaker.session']
                session['success_message'] = "Cadastro realizado com sucesso! Faça login."
                session.save()
                return self.redirect('/login')
            
            except ValueError as e:
                temp_user_data = {'name': request.forms.get('name'), 'email': request.forms.get('email')}
                return self.render('user_form', 
                                   user=temp_user_data, 
                                   action="/register", 
                                   validation_error=str(e))
            except Exception as e:
                return self.render('user_form', 
                                   user=None, 
                                   action="/register", 
                                   validation_error="Erro inesperado no cadastro.")


    def login(self):
        if request.method == 'GET':
            return self.render('login', login_error=None, user_data=None)
        else:
            session = request.environ['beaker.session']
            email = request.forms.get("email")
            password = request.forms.get("password")
            user_data = {'email': email}

            user, error = self.user_service.login_user(email, password) 
            
            if error:
                return self.render('login', login_error=error, user_data=user_data)

            session['user_id'] = user.id 
            session['logged_in'] = True
            session.save()
            
            session['success_message'] = f"Bem-vindo(a), {user.name}!"
            session.save()
            
            return self.redirect('/')


    def logout(self):
        session = request.environ['beaker.session']
        session.delete()
        
        session['info_message'] = "Você foi desconectado(a)."
        session.save()
        
        return self.redirect('/login')


    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            session = request.environ['beaker.session']
            session['error_message'] = "Usuário não encontrado."
            session.save()
            return self.redirect('/users')

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            try:
                self.user_service.edit_user(user)
                session = request.environ['beaker.session']
                session['success_message'] = f"Dados do usuário {user.name} atualizados."
                session.save()
                return self.redirect('/users')
            except ValueError as e:
                return self.render('user_form', 
                                   user=user, 
                                   action=f"/users/edit/{user_id}", 
                                   validation_error=str(e))


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        session = request.environ['beaker.session']
        session['success_message'] = f"Usuário ID {user_id} excluído com sucesso."
        session.save()
        self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)