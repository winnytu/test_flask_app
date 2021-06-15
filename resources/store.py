from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store: 
            return store.json()

        return {'messege':'Store not found'}, 400
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'messege':"Store with name '{}' already exist.".format(name)},400
        
        store = StoreModel(name)
        try: 
            store.save_to_db()
        except:
            return {'messege': 'somrthing wrong'},500

        return store.json(),201
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return{'messege':'store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}