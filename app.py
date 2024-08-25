import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)


# GET Get all stores
@app.get("/store")
def get_stores():
    return { "stores": list(stores.values()) }

# GET An indidivual Store
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try: 
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")
    
# POST Create a store
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    
    store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    
    return store, 201

# POST Create an item
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found.")
        
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    
    return item, 201

# GET all items
@app.get("/item")
def get_items():
    return { "items": list(items.values()) }

# GET An individual item
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")