import sqlite3
from flask import Flask,request,jsonify
from flask_restful import Resource,reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,create_refresh_token,
    get_jwt_identity
)
from models.item import ItemModel
class Item(Resource):   
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()     
        return {'messege':'item not found'}

    @jwt_required()
    def post(self,name):
        # 如果在items已經有同樣的name
        if ItemModel.find_by_name(name): 
            return {'messege': "An item with name '{}' already exists".format(name)}, 400   
        # 獲取body攜帶的json資料
        data = request.get_json()
        # name 在url price在body
        item = ItemModel(name,**data)
        try:
            item.save_to_db() 
        except:
            return {'messege':'as error occured inserting the item'},500

        return item.json(), 201
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'messege':'item deleted'}
    def put(self,name):
        data = request.get_json()
        
        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name,**data) 
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()
    

class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})
        # return items
        # connection.commit()
        # connection.close()
        return {'items':[item.json() for item in ItemModel.query.all()]}
        # return {'items':list(map(lambda x: x.json(),ItemModel.query.all()))}