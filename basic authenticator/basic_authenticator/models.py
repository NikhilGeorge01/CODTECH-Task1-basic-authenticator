from basic_authenticator import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from hashlib import md5
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128)) 
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        print("password is: ", password)
        print(f"Password hashed: {self.password_hash}") 
        print(check_password_hash(self.password_hash,password))

    def check_password(self, password):
      print(f"Stored password hash: {self.password_hash}")
      print(f"Password input to check: {password}")
      print(generate_password_hash(password))
      result = check_password_hash(self.password_hash, password)
      print(f"Password check result: {result}")
      return result

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)  

       