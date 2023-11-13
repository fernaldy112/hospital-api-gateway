from flask import Flask
app = Flask(__name__)

@app.route("/help", methods=["GET"])
def getHelp():
	return {"name": "grand-oak"}