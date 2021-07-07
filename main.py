from flask import Flask, render_template
app = Flask(__name__)





import pyrebase

config={
    "apiKey": "AIzaSyCRLMv7lriAw41uX4WlE7DIsS09icfkdyM",
    "authDomain": "techno-vedha.firebaseapp.com",
    "databaseURL": "https://techno-vedha-default-rtdb.firebaseio.com",
    "projectId": "techno-vedha",
    "storageBucket": "techno-vedha.appspot.com",
    "messagingSenderId": "622740569536",
    "appId": "1:622740569536:web:1be3a00fabc0a926645c25",
    "measurementId": "G-15Y1XM7TFH"
        }
firebase=pyrebase.initialize_app(config)
db=firebase.database()

db.update({"dust1":10})
db.update({"dust2":50})
db.update({"dust3":30})
db.update({"dust4":90})

users=db.get()
print(users.val()['dust1'])

@app.route('/')
def hello_world():

    

    dust1=users.val()['dust1']
    dust2=users.val()['dust2']
    dust3=users.val()['dust3']
    dust4=users.val()['dust4']
    return render_template("index.html",dust1=dust1,dust2=dust2,dust3=dust3,dust4=dust4)


app.run(debug=True)
