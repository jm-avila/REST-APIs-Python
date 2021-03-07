import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class ItemModel():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def json(self):
        return { "name": self.name, "price": self.price }
    
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        
        if row:
            return cls(*row)
    
    def upsert(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "REPLACE INTO items VALUES('{}', {})".format(self.name, self.price)
        cursor.execute(query)
        connection.commit()
        connection.close()
    
    def delete(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        query = "DELETE FROM items WHERE name='{}'".format(self.name)
        cursor.execute(query)
        connection.commit()
        connection.close()

class ItemListModel(Resource):
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
            items.append(ItemModel(*row).json())
        
        return items