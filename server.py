from flask import Flask, jsonify
import requests
import json


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


# @app.route("/info", methods=["GET"])
# def information():
#     x = "This website will calculate blood cholesterol levels.\n"
#     x += "It is written by David Ward."
#     return x

@app.route("/addnumbers", methods=["POST"])
def add_numbers():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    return jsonify(answer)


@app.route("/add/<a>/<b>", methods=["GET"])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)



if __name__ == "__main__":
    app.run()