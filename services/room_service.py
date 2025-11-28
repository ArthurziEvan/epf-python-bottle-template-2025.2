import random
import string

from bottle import request

from models.room import RoomModel, Room

class RoomService:

    def __init__(self):
        self.room_model = RoomModel()

    def get_all(self):
        rooms = self.room_model.get_all()
        return rooms


    def save(self):
        keys = string.ascii_uppercase + string.digits
        session = request.environ['beaker.session']
        host_id = session.get('user_id')

        while True:
            new_id = ''.join(random.choice(keys) for _ in range(6))

            if all(r.id != new_id for r in self.room_model.get_all()):
                break

        name = request.forms.get('name')

        room = Room(id=new_id, name=name, host_id=host_id, members=[host_id])
        self.room_model.add_room(room)


    def edit_room(self, room_id, room):
        if not self.room_model.get_by_id(room_id):
            raise ValueError("Erro: sala não existe.")

        self.room_model.update_room(room)
        return room


    def sort(self, room):
        members = room.members

        receivers = members.copy()

        if len(members) < 2:
            raise ValueError("Erro: a sala precisa ter no mínimo 4 membros")

        random.shuffle(members)
        att = 0
        while any(members[i] == receivers[i] for i in range(len(members))):
            random.shuffle(receivers)
            att += 1
            if att > 50:
                raise RuntimeError("Erro!")

        room.chosen = {
            members[i]: receivers[i]
            for i in range(len(members))
        }

        room.sorted = True
        self.room_model.update_room(room)



    def get_by_id(self, room_id):
        return self.room_model.get_by_id(room_id)


    def delete_room(self, room_id):
        self.room_model.delete_room(room_id)