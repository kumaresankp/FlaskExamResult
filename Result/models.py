from datetime import datetime,date
from Result import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(Regno):
    return User.query.get(int(Regno))

class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    semester = db.Column(db.Integer)
    exam_type = db.Column(db.String(100))
    subject1_marks = db.Column(db.Float)
    subject2_marks = db.Column(db.Float)
    subject3_marks = db.Column(db.Float)
    subject4_marks = db.Column(db.Float)
    subject5_marks = db.Column(db.Float)
    subject6_marks = db.Column(db.Float)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    Regno = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.Integer)
    code = db.Column(db.String(120), unique=True, nullable=False)