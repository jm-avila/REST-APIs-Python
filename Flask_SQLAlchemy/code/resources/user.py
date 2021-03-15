import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument("password",
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = self.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username already exists."}, 400
        
        try:
            user = UserModel(None, data["username"], data["password"])
            user.insert()
        except:
            return {"message": "An error occured inserting the user"}, 500
        
        return {"message": "User created successfully."}, 201