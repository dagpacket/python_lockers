from flask import jsonify
from Classes.Serial import Serial
from models import LockerModel
class Locker:
    def get_all(self, data):
        lockers = LockerModel.all()
        response = {
            'locker' : lockers
        }
        return jsonify(response)
    def get(self, data):
        print (data['scan'])
        return 1
    def open(self, data):
        serial = Serial()
        return serial.open(data['scan']);
    def is_loaded(self, data):
        print (data['scan'])
        return 1