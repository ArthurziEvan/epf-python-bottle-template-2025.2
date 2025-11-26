import json
import os


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Room:

    def __init__(self, id, name, host_id, members=None, chosen=None, sorted=False):
        self.id = id
        self.name = name
        self.host_id = host_id
        self.members = members or []
        self.chosen = chosen or {}
        self.sorted = sorted

    def __repr__(self):
        return f'<Room id={self.id} name={self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'host_id': self.host_id,
            'members': self.members,
            'chosen': self.chosen,
            'sorted': self.sorted
        }

    @classmethod
    def from_dict(cls, data):
        return Room(
            id=data['id'],
            name=data['name'],
            host_id=data['host_id'],
            members=data['members'],
            chosen=data['chosen'],
            sorted=data['sorted']
        )

class RoomModel:

    FILE_PATH = os.path.join(DATA_DIR, 'rooms.json')

    def __init__(self):
        self.rooms = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Room(**item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([r.to_dict() for r in self.rooms], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.rooms


    def get_by_id(self, room_id: int):
        return next((u for u in self.rooms if u.id == room_id), None)

    def add_room(self, room: Room):
         self.rooms.append(room)
         self._save()

    def update_room(self, updated_room: Room):
        for i, room in enumerate(self.rooms):
            if room.id == updated_room.id:
                self.rooms[i] = updated_room
                self._save()
                break

    def delete_room(self, room_id: int):
        self.rooms = [r for r in self.rooms if r.id != room_id]
        self._save()