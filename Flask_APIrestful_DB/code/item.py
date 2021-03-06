import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @classmethod
    def find_item_by_name(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"name": row[0], "price": row[1]}

    @classmethod
    def upsert(self, name, price):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        query = "REPLACE INTO items VALUES('{}', {})".format(name,price)
        cursor.execute(query)
        connection.commit()
        connection.close()
        
        return self.find_item_by_name(name)

    @classmethod
    def delete_by_name(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        query = "DELETE FROM items WHERE name='{}'".format(name)
        cursor.execute(query)
        connection.commit()
        connection.close()

    @jwt_required()
    def get(self, name):
        item = self.find_item_by_name(name)

        if item:
            return item
        
        return {"message": "Item of found"}, 404

    @jwt_required()
    def post(self, name):
        try:
            item = self.find_item_by_name(name)
        except:
            {"message": "An error occured while inserting the item."}, 500
        
        if item:
            return {"message": "An item with name '{}' already exists.".format(name)}, 404
        
        data = Item.parser.parse_args()
        price = data["price"]
        
        item = self.upsert(name, price)
        
        return  item, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        price = data["price"]
        
        try:
            item = self.upsert(name, price)
        except:
            {"message": "An error occured while upserting the item."}, 500
        
        return item, 201

    @jwt_required()
    def delete(self, name):
        try:
            self.delete_by_name(name)
        except:
            {"message": "An error occured while deleting the item."}, 500
        
        return {"message": "Item deleted"}

class ItemList(Resource):
    @classmethod
    def find_all_items(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        rows = result.fetchall()
        connection.close()

        items = []
        for row in rows:
            items.append({ "name": row[0], "price": row[1]})

        return items

    @jwt_required()
    def get(self):
        try:
            items = self.find_all_items()
        except:
            return {"message": "An error occured while getting the items."}, 500
        
        return items
