from pydantic import BaseModel

class InventoryItemBase(BaseModel):
    name: str
    category: str
    quantity: int
    price: float
    supplier: str

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemResponse(InventoryItemBase):
    id: int

    class Config:
        from_attributes = True