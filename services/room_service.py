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

        while True:
            new_id = ''.join(random.choice(keys) for _ in range(6))

            if all(r.id != new_id for r in self.room_model.get_all()):
                break

        name = request.forms.get('name')
        host_id = request.forms.get('host_id')

        room = Room(id=new_id, name=name, host_id=host_id)
        self.room_model.add_room(room)


    def sort(self, room_id):
        room = self.room_model.get_by_id(room_id)
        members = room.members

        if len(members) < 4:
            raise ValueError("Erro: a sala precisa ter no mínimo 4 membros")

        sorted_members = members[:]
        while True:
            random.shuffle(sorted_members)
            if all(g != r for g, r in zip(members, sorted_members)):
                break

        assignments = {g: r for g, r in zip(members, sorted_members)}

        room.chosen = assignments
        self.room_model.update_room(room_id)

        return assignments

    def get_by_id(self, room_id):
        return self.room_model.get_by_id(room_id)

    def delete_room(self, room_id):
        self.room_model.delete_room(room_id)