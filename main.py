from fastapi import FastAPI

app = FastAPI()


data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}, {"id": 3, "name": "Item 3"}, {"id": 4, "name": "Item 4"}, {"id": 5, "name": "Item 5"}]




@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get('/get-items')
def get_items(first_n: int = None):
    if first_n:
        return data[:first_n]
    else:
     return data


@app.get('/get-item/{item_id}')
def get_item(item_id: int):
    for item in data:
        if item["id"]== item_id:
            return item
    return {"error": "Item not found"}


@app.post('/add-item')
def add_item(item:dict):
    id = len(data) + 1
    new_item = {
        "id":id,
        "name": item["name"]
    }
    data.append(new_item)
    return new_item
    

        
@app.put('/update-item/{item_id}')
def update_item(item_id: int, item:dict):
    for itm in data:
        if itm["id"] == item_id:
            itm["name"] = item["name"]
            return itm        
    return {"error": "Item not found"}    


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    for idx in data:
        if idx["id"] == item_id:
            data.remove(idx)
            return {"message": "Item deleted successfully"}
    return {"error": "Item not found"}    