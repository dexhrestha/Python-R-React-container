from flask import Flask
import requests


app = Flask(__name__)


@app.route("/")
def home():
	return "Home"

@app.route("/writeData")
def writeData():
	with open('static/test.txt','w') as f:
		f.write('writing new data ')
	return "written new data to file"

@app.route("/runR")
def runR():
	res = requests.get("http://localhost:8001/")

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")