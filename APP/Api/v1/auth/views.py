from flask import request
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from ..models import User, users
from validators.validators import Validators

class SignUp(Resource):
    def post(self):
        """User can signup"""

        request_data = SignUp.parser.parse_args()
        fname = request_data['first_name']
        lname = request_data['last_name']
        username = request_data['username']
        email = request_data['email']
        password = request_data['password']
        confirm_password = request_data['confirm_password']


        if not Validators().valid_fname(first_name):
            return {
                'message':'enter a valid first_name'
            }, 401

        if not Validators().valid_lname(last_name):
            return {
                'message':'enter a valid last_name'
            }, 401

        if  User().get_user_by_username(username):
            return {
                "message":f"User with username {username} already exists"
            }

        if not Validators().valid_username(username):
            return {
                'message':'enter a valid username'
            }, 401

        if not Validators().valid_email(email):
            return {
                "message":"Enter a valid email"
            }, 401

        if not Validators().valid_password(password):
            return {
                'message':'Enter a valid password'
            }, 401

        if password != confirm_password:
            return {
                'message':'passwords do not match'
            }, 200

        user = User(first_name, last_name, username, email, password, confirm_password)
        users.append(user)

        return {
            'message':f'Account for {username} created successfully'
        }, 201

class Login(Resource):
    def post(self):
        """User can login"""

        request_data = Login.parser.parse_args()

        username = request_data['username']
        password = request_data['password']

        if not Validators().valid_username(username):
            return {
                'message':'enter a valid username'
            }, 401

        if not Validators().valid_password(password):
            return {
                'message':'Enter a valid password'
            }, 401

        user = User().get_user_by_username(username)
        if not user:
            return {
                'message':'user does not exist'
            }, 404
        if not check_password_hash(user.password, password):
            return {
                'message':'Invalid password, enter the correct password'
            }, 401

        return {
            'message':f'successfully logged in as {user.username}'
        }

