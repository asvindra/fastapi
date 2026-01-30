from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel,Field
from enum import IntEnum

app = FastAPI()


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=500,description="Name of the item")
    description: Optional[str] = Field(None, max_length=1000, description="Description of the item")
    priority: Priority = Field(Priority.LOW, description="Priority of the item")     

class ItemCreate(ItemBase):
    pass    

class Item(ItemBase):
    id: int = Field(...,description="ID of the item")
class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=500,description="Name of the item")
    description: Optional[str] = Field(None, max_length=1000, description="Description of the item")
    priority: Optional[Priority] = Field(None, description="Priority of the item")
    







data = [Item(id=1, name="Item 1",priority=Priority.LOW), Item(id=2, name="Item 2",priority=Priority.MEDIUM), Item(id=3, name="Item 3",priority=Priority.HIGH), Item(id=4, name="Item 4",priority=Priority.LOW   )]




@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get('/get-items',response_model=List[Item])
def get_items(first_n: int = None):
    if first_n:
        return data[:first_n]
    else:
     return data


@app.get('/get-item/{item_id}',response_model=Item)
def get_item(item_id: int):
    for item in data:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post('/add-item',response_model=Item)
def add_item(item:ItemCreate):
    id = len(data) + 1
    new_item = Item( 
        id=id,
        name=item.name,
        description=item.description,
        priority=item.priority
    )
    data.append(new_item)
    return new_item
    

        
@app.put('/update-item/{item_id}',response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    for itm in data:
        if itm.id == item_id:
            itm.name = item.name
            itm.description = item.description
            itm.priority = item.priority
            return itm        
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/delete-item/{item_id}",response_model= Item)
def delete_item(item_id: int):
    for idx, item in enumerate(data):
        if item.id == item_id:
            deleItem =  data.pop(idx)
            return deleItem
    raise HTTPException(status_code=404, detail="Item not found") 