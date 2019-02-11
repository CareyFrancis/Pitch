# from builtins import classmethod
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch(db.Model):
    '''
    Pitch class to define our classes
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    category_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def save_pitch(self):
        """
        Function to save pitches
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls):
        """
        Function that quries database and returns all pitches
        """
        return Pitch.query.all()

    @classmethod
    def get_pitch_by_category(cls, cat_id):
        """
        Function that queries the database and returns the pitches based on category
        """
        return Pitch.query.filter_by(category_id = cat_id)

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

