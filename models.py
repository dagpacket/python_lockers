from app import db

import datetime

class LockerModel(db.Model):
    __table_name__ = 'lockers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    loaded = db.Column(db.Bolean, default=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, loaded):
        self.name = name
        self.loaded = loaded
        self.updated_at = datetime.datetime.now().timestamp()
    @staticmethod
    def create(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    def all():
        return Locker.query.all()
    @staticmethod
    def get_by_id():
        return Locker.query.get(id)



if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")