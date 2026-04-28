from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Inventory Manager API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "AI Inventory Manager API is running"}

@app.post("/items", response_model=schemas.InventoryItemResponse)
def create_item(item: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    new_item = models.InventoryItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/items", response_model=List[schemas.InventoryItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(models.InventoryItem).all()

@app.get("/items/{item_id}", response_model=schemas.InventoryItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=schemas.InventoryItemResponse)
def update_item(item_id: int, updated_item: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in updated_item.dict().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/low-stock")
def low_stock(db: Session = Depends(get_db)):
    items = db.query(models.InventoryItem).filter(models.InventoryItem.quantity < 10).all()
    return items

@app.get("/ai-recommendation/{item_id}")
def ai_recommendation(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if item.quantity < 5:
        recommendation = f"Urgent restock needed for {item.name}. Current quantity is very low."
    elif item.quantity < 10:
        recommendation = f"Consider restocking {item.name} soon."
    else:
        recommendation = f"{item.name} stock level is healthy."

    return {
        "item": item.name,
        "quantity": item.quantity,
        "recommendation": recommendation
    }