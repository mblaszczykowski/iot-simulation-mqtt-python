from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Item as DBItem
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    value: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    items = db.query(DBItem).all()
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/value/{min_value}")
def get_items_by_value(min_value: float, db: Session = Depends(get_db)):
    items = db.query(DBItem).filter(DBItem.value > min_value).all()
    return items

@app.post("/items")
def add_item(item: Item, db: Session = Depends(get_db)):
    db_item = DBItem(id=item.id, name=item.name, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.value = item.value
        db.commit()
        db.refresh(db_item)
        return db_item
    raise HTTPException(status_code=404, detail="Item not found")
