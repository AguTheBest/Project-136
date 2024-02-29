from flask import Flask,jsonify,request
from data1 import data
app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({
        "data":data,
        "message":"success",
        
    }),200

@app.route("/stars")
def planet():
    name=request.args.get("name")
    for item in data:
        if(item["name"]==name):
          return jsonify({
            "data":item,
            "message":"success",
        
          }),200


if __name__ == "__main__":
    app.run()