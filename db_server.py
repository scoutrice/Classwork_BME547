# db_server.py

'''
Database format

[{
    "name": <string>,
    "id": <integer>,
    "blood_type": <string>,
    "test_name": [<string1>, <string2>, ...],
    "test_result": [<string1>, <string2>, ...]
}]

'''

db = []

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_on():
    return "DB server is on."


def add_patient(patient_name, patient_id, blood_type):
    new_patient = {"name": patient_name,
                   "id": patient_id,
                   "blood_type": blood_type,
                   "test_name": [],
                   "test_results": []}
    db.append(new_patient)


def init_server():
    add_patient("Ann Ables", 1, "A+")
    add_patient("Bob Boyles", 2, "B+")
    # initialize logging     


@app.route("/new_patient", methods=["POST"])
def add_new_patient_to_server():
    """
    Three things this function should do:
    1. Receive data from POST requests
    2. Call other functions to do all the work
    3. Return information
    """
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400
    add_patient(in_data["name"],
                in_data["id"],
                in_data["blood_type"])
    return "Patient successfully added", 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary."
    expected_keys = ["name", "id", "blood_type"]
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data.".format(key)
    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return "Key {}'s value has the wrong data type.".format(key)
    return True


if __name__ == "__main__":
    init_server()
    app.run()
