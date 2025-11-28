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

    # Rotas Sala
    def setup_routes(self):
        self.app.route('/rooms', method='GET', callback=lock_login(self.list_rooms))
        self.app.route('/rooms/add', method=['GET', 'POST'], callback=lock_login(self.add_room))
        self.app.route('/rooms/delete/<room_id>', method='POST', callback=lock_login(self.delete_room))
        self.app.route('/rooms/join', method=['GET', 'POST'], callback=lock_login(self.join_room))

        self.app.route('/rooms/<room_id>', method=['GET', 'POST'], callback=lock_login(self.room))

    def list_rooms(self):
        user = get_user_login(self.user_service)

        rooms = [
            r for r in self.room_service.get_all()
            if r.host_id == user.id or user.id in r.members
        ]

        return self.render('rooms', rooms=rooms, user=user)

    def add_room(self):
        if request.method == 'GET':
            return self.render('room_form', rooms=None, user=get_user_login(self.user_service), action="/rooms/add")
        else:
            self.room_service.save()
            return self.redirect('/rooms')


    def join_room(self):
        if request.method == 'GET':
            return self.render('join_room', user=get_user_login(self.user_service))
        else:
            user = get_user_login(self.user_service)
            room_id = request.forms.get('room_id')

            room = self.room_service.get_by_id(room_id)

            if not room:
                return self.render('join_room', error="Sala não encontrada.", user=user)

            if user.id == room.host_id or user.id in room.members:
                return self.render('join_room', error="Você já é membro dessa sala.", user=user)

            room.members.append(user.id)
            self.room_service.edit_room(room_id, room)
            return self.redirect('/rooms/<room_id>')


    def delete_room(self, room_id):
        self.room_service.delete_room(room_id)
        self.redirect('/rooms')

    def room(self, room_id):

        user=user=get_user_login(self.user_service)
        room = self.room_service.get_by_id(room_id)
        users = {u.id: u.name for u in self.user_service.get_all()}

        if user.id != room.host_id and user.id not in room.members:
            return self.home_redirect()

        return self.render('room', room=room, user=user, users=users)


    def sort(self, room_id):
        try:
            sorted = self.room_service.sort(room_id)
        except ValueError as e:
            return f"<h2>Erro : {str(e)}</h2>"



        # USO PARA MANDAR POR EMAIL NO FUTURO
            #for giver, reciever in sorted.items():
            user = self.user_service.get_by_id(reciever)


        return self.render('room_sort', sorted=sorted, user=get_user_login(self.user_service))


room_routes = Bottle()
room_controller = RoomController(room_routes)

