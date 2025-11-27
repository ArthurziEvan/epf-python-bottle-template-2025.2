from bottle import request, redirect

from services.user_service import UserService

user_service = UserService()

def lock_login(func):
    def wrap(*args, **kwargs):
        session = request.environ['beaker.session']
        if not session or 'user_id' not in session:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrap

def get_user_login():
    session = request.environ['beaker.session']
    if not session:
        return None
    user_id = session.get('user_id')
    if not user_id:
        return None
    return user_service.get_by_id(user_id)