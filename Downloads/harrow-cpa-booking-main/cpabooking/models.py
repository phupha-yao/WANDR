from cpabooking import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable = False)
    tutor_group = db.Column(db.String(5), nullable = False)
    bookings = db.relationship('Bookings', backref='user', lazy=True)
    
    
    def __repr__(self):
        return f"({self.id}, {self.email}, {self.username}, {self.tutor_group})"
        
class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.String(5), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    num_people = db.Column(db.Integer, nullable=False)
    time_slot= db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"({self.id}, {self.rid}, {self.uid}, {self.date}, {self.time_slot})"

# class Rooms(db.Model):
#     rid = db.Column(db.String(4), primary_key=True)

