from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():

    dust1=70
    dust2=60
    dust3=90
    dust4=40
    return render_template("index.html",dust1=dust1,dust2=dust2,dust3=dust3,dust4=dust4)


app.run(debug=True)