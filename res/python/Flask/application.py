from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World"

@app.route("/isabel")
def isabel():
	return "Hi Isabel, how was your day?"

