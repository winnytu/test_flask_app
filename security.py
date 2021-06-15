from flask import Flask,request,jsonify
from werkzeug.security import safe_str_cmp
from flask_restful import Resource,reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,create_refresh_token,
    get_jwt_identity
)
from models.user import UserModel
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = UserModel.find_by_username(username)
        if user and safe_str_cmp(user.password,password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)