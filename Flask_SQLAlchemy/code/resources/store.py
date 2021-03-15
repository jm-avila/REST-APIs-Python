from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        
        if store:
            return store.json()
        
        return {"message": "Store not of found"}, 404

    @jwt_required()
    def post(self, name):
        store = StoreModel.find_by_name(name)
        
        if store:
            return {"message": "An store with name '{}' already exists.".format(name)}, 404
        
        try:
            store = StoreModel(name)
            store.upsert()
        except:
            {"message": "An error occured while inserting the store."}, 500
        
        
        return  store.json(), 201

    @jwt_required()
    def delete(self, name):
        try:
            store = StoreModel.find_by_name(name)
            if store:
                store.delete()
        except:
            {"message": "An error occured while deleting the store."}, 500
        
        return {"message": "Item deleted"}

class StoreList(Resource):
    @jwt_required()
    def get(self):
        try:
            return [store.json() for store in StoreModel.query.all()]
        except:
            return {"message": "An error occured while getting the stores."}, 500
        
        return items
