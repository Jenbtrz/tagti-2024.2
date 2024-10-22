#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

<<<<<<< HEAD
@app.route('/')
def index():
    return render_template("contato.hmtl")
=======
@app.route("/contato")
def contato():
    return render_template("contato.html")
>>>>>>> d5477831f052034a1dc9fb8f3a83977194d7fdc1

if __name__ == '__main__':
    app.run()
