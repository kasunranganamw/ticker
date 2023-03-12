from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome() :
    return "Welcome to Python Webservice"

@app.route("/ticker/<symbol>", methods=['POST'])
def getTickerData(symbol) :
    print("get ticker data")
    return jsonify({"data": "test data"})

if (__name__=="__main__") :
    app.run()

