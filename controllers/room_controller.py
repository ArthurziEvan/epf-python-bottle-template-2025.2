from bottle import request, Bottle
from isort.literal import assignments

from controllers.base_controller import BaseController
from services.auth_service import lock_login, get_user_login
from services.room_service import RoomService
from services.user_service import UserService


class RoomController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.room_service = RoomService()
        self.user_service = UserService()

    # Rotas Sala
    def setup_routes(self):
        self.app.route('/rooms', method='GET', callback=self.list_rooms)
        self.app.route('/rooms/add', method=['GET', 'POST'], callback=lock_login(self.add_room))
        self.app.route('/rooms/delete/<room_id>', method='POST', callback=lock_login(self.delete_room))

        self.app.route('/rooms/<room_id>', method=['GET', 'POST'], callback=lock_login(self.room))

    def list_rooms(self):
        rooms = self.room_service.get_all()
        return self.render('rooms', rooms=rooms)

    def add_room(self):
        if request.method == 'GET':
            return self.render('room_form', rooms=None, user=get_user_login(), action="/rooms/add")
        else:
            self.room_service.save()
            return self.redirect('/rooms')

    def delete_room(self, room_id):
        self.room_service.delete_room(room_id)
        self.redirect('/rooms')

    def room(self, room_id):

        room = self.room_service.get_by_id(room_id)
        return self.render('room', room=room, user=get_user_login())

    def sort(self, room_id):
        try:
            sorted = self.room_service.sort(room_id)
        except ValueError as e:
            return f"<h2>Erro : {str(e)}</h2>"



        # USO PARA MANDAR POR EMAIL NO FUTURO
            #for giver, reciever in sorted.items():
            user = self.user_service.get_by_id(reciever)


        return self.render('room_sort', sorted=sorted, user=get_user_login())


room_routes = Bottle()
room_controller = RoomController(room_routes)

