from flask_sqlalchemy import SQLAlchemy

class Database:
    def __init__(self):
        db = SQLAlchemy()
        return db
