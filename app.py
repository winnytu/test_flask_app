import os

from security import Login
from flask import Flask
from flask_restful import Api
# resource creating some data
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,create_refresh_token,
    get_jwt_identity
)
from werkzeug.security import safe_str_cmp
from resources.user import UserRegister
from resources.item import Item,ItemList 
from resources.store import Store,StoreList
from db import db

app = Flask(__name__)
uri = os.environ.get("DATABASE_URL",'sqlite:///data.db')   # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'this-should-be-change'
db.init_app(app)
api = Api(app)

# create table
@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

api.add_resource(Item,'/item/<string:name>') 
api.add_resource(ItemList,'/Items')
api.add_resource(Login,'/login')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

# 只要在run這個檔案的時候才會執行 沒加的話則是import的時候就會執行
if __name__ == "__main__":
    app.run(port=5000)