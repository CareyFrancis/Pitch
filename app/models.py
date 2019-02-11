# from builtins import classmethod
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch:
    '''
    Pitch class to define our classes
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), index=True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='pitch', lazy='dynamic')

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.order_by(pitch_id=id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'




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


# class Comment:
    #
    # all_reviews = []
    #
    # def __init__(self,movie_id,title,imageurl,review):
    #     self.movie_id = movie_id
    #     self.title = title
    #     self.imageurl = imageurl
    #     self.review = review
    #
    #
    # def save_review(self):
    #     Review.all_reviews.append(self)
    #
    #
    # @classmethod
    # def clear_reviews(cls):
    #     Review.all_reviews.clear()
    #
    # @classmethod
    # def get_reviews(cls,id):
    #
    #     response = []
    #
    #     for review in cls.all_reviews:
    #         if review.movie_id == id:
    #             response.append(review)
    #
    #     return response
