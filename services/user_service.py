from bottle import request
from passlib.handlers.bcrypt import bcrypt
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()


    def get_all(self):
        users = self.user_model.get_all()
        return users


    def save(self):
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        email = request.forms.get('email')
        password_hash = pbkdf2_sha256.hash(request.forms.get('password'))

        user = User(id=new_id, name=name, email=email, password=password_hash)
        self.user_model.add_user(user)

        session = request.environ['beaker.session']
        session['user_id'] = user.id
        session.save()


    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)


    def get_by_email(self, email):
        return self.user_model.get_by_email(email)


    def edit_user(self, user):
        name = request.forms.get('name')
        email = request.forms.get('email')
        password_hash = pbkdf2_sha256.hash(request.forms.get('password'))

        user.name = name
        user.email = email
        user.password = password_hash

        self.user_model.update_user(user)


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)


    def login_user(self, email, password):
        users = self.user_model.get_all()

        for user in users:
            if user["email"].lower() == email.lower():
                if bcrypt.verify(password, user["password"]):
                    return user, None
                else:
                    return None, "Senha Incorreta."

        return None, "Email Inválido."