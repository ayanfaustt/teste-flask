from crypt import methods
from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


user_data = {
    1:{
        "id": 1,
        "name":"Paulo"
    },
    2:{
        "id": 1,
        "name":"Paulo"
    }

}


def response_users():
    return {"users": user_data}


@app.route('/')
def root():
    return "<h1> API com Flask </h1>"

@app.route('/users')
def list_users():
    return response_users()

@app.route("/users", methods=["POST"])
def create_user():
    body = request.json

    ids = list(user_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1

    user_data[new_id] = {
        "id": new_id,
        "name": body["name"]
    }

    return response_users()

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete(user_id: int):
    user = user_data.get(user_id)

    if user:
        del user_data[user_id]
    
    return response_users()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update(user_id: int):
    body = request.json
    name = body.get("name")
    
    user = user_data.get(user_id)

    if user_id in user_data:
        user_data[user_id]["name"] = name
    
    return response_users()

app.run(debug = True)