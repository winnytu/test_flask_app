# included rescource 使用者互動 但不會汙染resource
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field cannot be blank"
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field cannot be blank"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'messega':'A user with the username is already exist'}
        user = UserModel(**data) # each key in data
        user.save_to_db()

        return {'messege':'user created successfully'}, 201