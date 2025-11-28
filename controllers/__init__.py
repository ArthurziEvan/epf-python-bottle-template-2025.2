from bottle import Bottle

from controllers.home_controller import home_routes
from controllers.room_controller import room_routes
from controllers.user_controller import user_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(room_routes)
    app.merge(home_routes)