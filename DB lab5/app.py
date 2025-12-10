from app import create_app
from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = create_app()


SECRET_KEY = "qazxswedcvfrtgbnhy"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401
        return f(*args, **kwargs)
    return decorated


@app.route('/login', methods=['POST'])
def login():
    auth_data = request.get_json()
    username = auth_data.get("username")
    password = auth_data.get("password")

    if username == "admin" and password == "password":
        token = jwt.encode({
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({"message": "This is protected!"})

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)

