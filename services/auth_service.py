
from bottle import request, redirect

from services.user_service import UserService

def lock_login(func):
    def wrap(*args, **kwargs):
        session = request.environ['beaker.session']
        if not session or 'user_id' not in session:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrap

def get_user_login(user_service):
    session = request.environ['beaker.session']

    logged_user = None

    if session and session.get('user_id'):
        user_id = session['user_id']
        logged_user = user_service.get_by_id(user_id)

    return logged_user
