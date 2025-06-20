from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_of_birth = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    password = db.Column(db.String(128), nullable=False)  # Store hashed passwords

    def __repr__(self):
        return f'<User {self.username}>' 