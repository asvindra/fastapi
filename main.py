from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from pydantic import BaseModel,Field
from enum import IntEnum
from db import engine,get_db
from models import Base, Todos
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
class TodoBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=500,description="Name of the todo")
    description: Optional[str] = Field(None, max_length=1000, description="Description of the todo")
    priority: Priority = Field(Priority.LOW, description="Priority of the todo")     

class TodoCreate(TodoBase):
    pass    

class Todo(TodoBase):
    id: int = Field(...,description="ID of the Todo")
class TodoUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=500,description="Name of the todo")
    description: Optional[str] = Field(None, max_length=1000, description="Description of the todo")
    priority: Optional[Priority] = Field(None, description="Priority of the todo")
    





#root path
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

#To get the todos 
@app.get('/get-todos',response_model=List[Todo])
def get_todos(first_n: int = None,db:Session = Depends(get_db)):
   items = db.query(Todos).all()
   return items

#To get the todo 
@app.get('/get-todo/{todo_id}',response_model=Todo)
def get_todo(todo_id: int,db:Session = Depends(get_db)):
    item = db.query(Todos).filter(Todos.id== todo_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found") 
    return item


#To Create the todo 
@app.post('/add-todo',response_model=Todo)
def add_todo(item:TodoCreate,db:Session = Depends(get_db)):
    new_item = Todos( 
        name=item.name,
        description=item.description,
        priority=item.priority
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
    


#To update the todo 
@app.put('/update-todo/{todo_id}',response_model=Todo)
def update_todo(todo_id: int, item: TodoUpdate, db:Session = Depends(get_db)):
    elmItem = db.query(Todos).filter(Todos.id == todo_id).first()
  
    if not elmItem:
     raise HTTPException(status_code=404, detail="Item not found")
    
    if item.name is not None:
        elmItem.name = item.name
    if item.description is not None:
        elmItem.description = item.description
    if item.priority is not None:
        elmItem.priority = item.priority   
        
    db.commit()
    db.refresh(elmItem)         
    return elmItem


#To delete the todo
@app.delete("/delete-todo/{todo_id}",response_model= Todo)
def delete_todo(todo_id: int,db:Session = Depends(get_db)):
    item = db.query(Todos).filter(Todos.id== todo_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found") 
    db.delete(item)
    db.commit()
    return item