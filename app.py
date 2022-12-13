#pip install flask
#pip install flask-restful
#pip install flask-cors
#pip install flask-sqlalchemy
#pip install psycopg2
#pip install flask-migrate
#pip list
# flask.exe db init
#flask.exe db migrate
#flask.exe db upgrade

#https://www.youtube.com/watch?v=a7V2zBy6i7w&t=803s


from flask import Flask,request
from flask_restful import Resource,Api 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

api=Api(app)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:c98xa5@localhost:5432/flask_api'

db=SQLAlchemy(app)

migrate=Migrate(app,db)

class UserModel(db.Model):
    tablename='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String())
    password=db.Column(db.String())
    email=db.Column(db.String(),unique=True,nullable=False)

def init(self,username,password,email):
    self.username=username
    self.password=password
    self.email=email

def repr(self):
    return f"<User {self.username}>"

@app.route("/users",methods=['POST','GET'])
def users():
    if request.method=='POST':
        if request.is_json:
            data=request.get_json()
            new_user=UserModel(
                username=data['username'],
                password=data['password'],
                email=data['email']
            )
            db.session.add(new_user)
            db.session.commit()
            return {"messages":f"user {new_user.username} with email {new_user.email} has been created succesfully"}
        else:
            return{"error":"The request payload is not in JSON format"}
    elif request.method=='GET':
        users=UserModel.query.all()
        results = [ 
            {
                "username":user.username,
                "password":user.password,
                "email":user.email
            } for user in users
        ]

        return {"users":results}
