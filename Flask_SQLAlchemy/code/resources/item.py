from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument("store_id",
        type=int,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        
        if item:
            return item.json()
        
        return {"message": "Item of not found"}, 404

    @jwt_required()
    def post(self, name):
        item = ItemModel.find_by_name(name)
        
        if item:
            return {"message": "An item with name '{}' already exists.".format(name)}, 404
        
        data = Item.parser.parse_args()
        
        try:
            item = ItemModel(None, name, **data)
            item.upsert()
        except:
            {"message": "An error occured while inserting the item."}, 500
        
        
        return  item.json(), 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        price = data["price"]
        store_id = data["store_id"]

        item = ItemModel.find_by_name(name)
        
        if item:
            item.price = price
            item.store_id = store_id
        else:
            item = ItemModel(None, name, price, store_id)

        try:
            item.upsert()
        except:
            {"message": "An error occured while upserting the item."}, 500
        
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        try:
            item = ItemModel.find_by_name(name)
            if item:
                item.delete()
        except:
            {"message": "An error occured while deleting the item."}, 500
        
        return {"message": "Item deleted"}

class ItemList(Resource):
    @jwt_required()
    def get(self):
        try:
            return [item.json() for item in ItemModel.query.all()]
        except:
            return {"message": "An error occured while getting the items."}, 500
        
        return items
