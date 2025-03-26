from flask import Flask, request, jsonify


app=Flask(__name__)

@app.route("/",methods=["GET"])
def get_data():
    return "<h1>Welcome to Python , Port 5000</h1>"

if __name__ == '__main__' :
    app.run(host="0.0.0.0",port=5000,debug=True)
