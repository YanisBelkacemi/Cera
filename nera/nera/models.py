
from nera import db ,login
from flask_login import UserMixin

from datetime import datetime

@login.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))





class post(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    text = db.Column(db.String() , nullable=False)
    author= db.Column(db.String(), nullable = False)
    date = db.Column(db.DateTime(), default = datetime.utcnow())


    def formatdate(self):
        return self.date.strftime("%d/%m/%Y at %H:%M:%S ")
    
    
class user(db.Model ,UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    Email = db.Column(db.String())
    ip = db.Column(db.String())
        


    def check_pass(self, entpassword):
        if entpassword== self.password:
            return True


